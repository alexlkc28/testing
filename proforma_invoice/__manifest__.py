# -*- coding: utf-8 -*-
###################################################################################
#
#    Aboutknowledge (Hong Kong) Limited.
#
#    Copyright (C) 2022-TODAY Aboutknowledge (Hong Kong) Limited (<https://www.cybrosys.com>).
#    Author: Aboutknowledge (Hong Kong) Limited (<https://www.aboutknowledge.com/>)


###################################################################################

{
    'name': 'Proforma Invoice',
    'version': '15.0.1.0.0',
    'summary': """Proforma Invoice""",
    'description': """This module is used to merge two sale orders in PI.""",
    'category': "Generic Modules/Human Resources",
    'author': 'Aboutknowledge (Hong Kong) Limited',
    'company': 'Aboutknowledge (Hong Kong) Limited',
    'website': "https://www.aboutknowledge.com/",
    'depends': ['base', 'account', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
