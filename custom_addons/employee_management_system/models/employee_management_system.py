# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError,ValidationError
from datetime import date


class Department(models.Model):
    _name = 'emp.department'
    _description = 'Department Model'

    name = fields.Char(string='Department Name', required=True)
    employee_ids = fields.One2many('emp.employee', 'department_id', string='Employees')
    hod_id = fields.Many2one('emp.employee', string='Head of Department')


class Employee(models.Model):
    _name = 'emp.employee'
    _description = 'Employee Model'
    _rec_name = 'full_name'

    first_name = fields.Char(string='First Name', required='True')
    last_name = fields.Char(string='Last Name',required='True')
    full_name = fields.Char(string='Full Name', compute='_compute_full_name', store=True)
    email = fields.Char(string='Email',required='True')
    phone = fields.Char(string='Phone',required='True')
    date_of_birth = fields.Date(string='Date of Birth',required='True')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender',required='True')
    address = fields.Text(string='Address',required='True')
    hire_date = fields.Date(string='Hire Date',required='True')
    salary = fields.Float(string='Salary')
    department_id = fields.Many2one('emp.department', string='Department',required='True')
    hod_name = fields.Char(string='Head of Department', compute='_compute_hod_name', store=True)

    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Email must be unique!'),
        ('positive_age', 'CHECK(age >= 0)', 'Age must be positive!'),
    ]
    status = fields.Selection([
        ('intern', 'Intern'),
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
        ('manager', 'Manager'),
    ], string='Status', default='intern')

    skill_ids = fields.Many2many(
        'emp.skill',
        'emp_employee_skill_rel',
        'employee_id',
        'skill_id',
        string='Skills'
    )

    @api.depends('department_id')
    def _compute_hod_name(self):
        for rec in self:
            if rec.department_id and rec.department_id.hod_id:
                rec.hod_name = rec.department_id.hod_id.full_name
            else:
                rec.hod_name = ''


    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                dob = record.date_of_birth
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = age
            else:
                record.age = 0

    @api.onchange('hire_date')
    def _onchange_hire_date(self):
        if self.hire_date and self.hire_date < fields.Date.to_date('2025-01-01'):
            return {
                'warning': {
                    'title': "Invalid Hire Date",
                    'message': "Hire Date cannot be before January 1, 2025.",
                }
            }

    @api.constrains('phone', 'email')
    def _check_phone_and_email(self):
        for record in self:
            if record.phone and (not record.phone.isdigit() or len(record.phone) != 10):
                raise ValidationError("Phone number must be exactly 10 digits.")
            if record.email and '@' not in record.email:
                raise ValidationError("Email must contain '@' symbol.")

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            record.full_name = (record.first_name or '') + ' ' + (record.last_name or '')

    def action_promote(self):
        promotion_order = ['intern', 'junior', 'senior', 'lead', 'manager']
        for record in self:
            current_index = promotion_order.index(record.status)
            if current_index < len(promotion_order) - 1:
                record.status = promotion_order[current_index + 1]
                if record.status == 'manager':
                    raise UserError(_("Now you are the Manager"))
            else:
                raise UserError(_("Promotion not possible. Already at highest status."))

    def action_view_skills(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Skills',
            'res_model': 'emp.skill',
            'view_mode': 'list,form',
            'domain': [('employee_ids', '=', self.id)],
            'context': {'default_employee_id': self.id},
            'target': 'current',
        }


    def create_record(self):
        print("Create Records")
        vals = {
            'first_name': self.first_name or '',
            'last_name': self.last_name or '',
            'phone':'',
            'date_of_birth': self.date_of_birth or '',
            'gender': self.gender or '',
            'address':'',
            'hire_date': fields.Date.context_today(self),
            'salary': 5000.0,
        }
        rec = self.env['emp.employee'].create(vals)
        print("Record:", rec)
        return rec

    def update(self):
        print("Update Records")
        employee_ids = self.env['emp.employee'].search([('first_name', '=', 'Ravi')]).ids
        employees = self.env['emp.employee'].browse(employee_ids)
        employees.write({'last_name': 'Sharma'})

    def search_method(self):
        print("Search Records")
        employees = self.env['emp.employee'].browse([1, 2, 3])
        employee = self.env['emp.employee'].search([('first_name','=','Ravi')])
        employee1 = self.env['emp.employee'].search_count([('first_name', '=', 'Ravi')])
        employee2 = self.env['emp.employee'].search_read([('first_name', '=', 'Ravi')], fields=['first_name', 'last_name'], limit=3)
        employee3 = self.env['emp.employee'].name_search('Ravi', limit=3)
        employee4 = self.env['emp.employee'].read_group(
            domain=[('gender', '=', 'male')],
            fields=['salary:sum', 'address'],
            groupby=['address']
        )

        print("Employee:", employees)
        print("Employee:", employee)
        print("Employee:", employee1)
        print("Employee:", employee2)
        print("Employee:", employee3)
        print("Employee:", employee4)

    def delete_method(self):
        print("Deleting employee records with first_name = 'John'...")
        employees = self.env['emp.employee'].search([('first_name', '=', 'John')])

        if employees:
            count = len(employees)
            employees.unlink()
            print(f"Deleted {count} employee record(s).")
        else:
            print("No employee records found to delete.")
