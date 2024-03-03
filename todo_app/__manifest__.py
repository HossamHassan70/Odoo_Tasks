# -*- coding: utf-8 -*-
{
    'name': "To Do",
    'summary': """This is Sammary""",
    'description': """Todo App for you, make your tasks more effictive""",
    'author': "Hossam Hassan",
    'version': '17.0.0.1.0',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/todo_ticket.xml',
    ],
    # 'application': True,
}