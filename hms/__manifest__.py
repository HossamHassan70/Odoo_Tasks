# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management System',
    'version': '1.0',
    'author': 'Hossam Hassan',
    'summary': 'Manage patients, doctors, appointments, and medical records in a hospital.',
    'description': """This module provides a comprehensive Hospital Management System (HMS) for managing various aspects of a hospital, including patients, doctors, appointments, and medical records. It includes features such as patient registration, appointment scheduling, medical history tracking, and billing.""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
    ],
    'application': True,
}