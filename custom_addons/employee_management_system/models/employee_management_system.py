# -*- coding: utf-8 -*-
from odoo import models, fields


class Department(models.Model):
    _name = 'emp.department'
    _description = 'Department Model'

    name = fields.Char(string='Department Name', required=True)
    employee_ids = fields.One2many('emp.employee', 'department_id', string='Employees')


class Employee(models.Model):
    _name = 'emp.employee'
    _description = 'Employee Model'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    address = fields.Text(string='Address')
    hire_date = fields.Date(string='Hire Date', required=True)
    salary = fields.Float(string='Salary', required=True)
    position = fields.Char(string='Position', required=True)
    department_id = fields.Many2one('emp.department', string='Department', required=True)

    skill_ids = fields.Many2many(
        'emp.skill',
        'emp_employee_skill_rel',
        'employee_id',
        'skill_id',
        string='Skills'
    )