# -*- coding: utf-8 -*-
{
    'name': "ABK Order Process",

    'summary': """
        ABK Order Custom""",

    'description': """
        ABK Order Custom
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'sale'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
