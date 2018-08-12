# -*- coding: utf-8 -*-
{
    'name': "Ajustes Modificado",

    'summary': """
        Practica nivel basico""",

    'description': """
        Modificaciones al modulo de ajustes
    """,

    'author': "victor magallanes",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv'
        # ,
        'views/edit_field.xml',        
        'views/position_field.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}