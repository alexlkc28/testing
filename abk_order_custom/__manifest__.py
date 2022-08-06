# -*- coding: utf-8 -*-
{
    'name': "abk_order_custom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/brand.xml',
        'views/fsc_claim.xml',
        'views/head_analysis.xml',
        'views/hs_commodity.xml',
        'views/material_analysis.xml',
        'views/product_class.xml',
        'views/reference_category.xml',
        'views/warranty.xml',
        'views/mrp_bom.xml',
    ],
}
