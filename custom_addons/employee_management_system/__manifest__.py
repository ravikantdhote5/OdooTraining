# -*- coding: utf-8 -*-

{
    'name': 'Employee Management',
    'version': '1.0',
    'summary': 'Manage Employees and Departments',
    'description': """
        This module allows you to manage employees and their departments,
        including personal and job-related information.
    """,
    'category': 'Human Resources',
    'author': 'Ravikant',
    'website': 'https://yourcompanywebsite.com',
    'depends': ['base'],
    'data': [
        'security/emp_groups.xml',
        'security/ir.model.access.csv',
        'views/employee_management_system_menus.xml',
        'views/employee_management_system_views.xml',
        'views/employee_skills_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}