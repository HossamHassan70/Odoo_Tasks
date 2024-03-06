# -*- coding: utf-8 -*-
{
    'name': "HMS",
    'description': "Hospital Mamagement System",
    'aurthor': 'Hossam Hassan',
    'version': "17.0.0.1.0",
    'depends': ['base'],
    'application': True,
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hms_patient.xml',
        'views/patient_menus.xml',
        'views/hms_department.xml',
        'views/hms_doctors.xml',
        'views/hms_logging.xml',
        'views/crm_customer_view.xml',
        'reports/patient_report.xml',
    ]
}
