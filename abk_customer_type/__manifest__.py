# -*- coding: utf-8 -*-
{
    'name': "ABK Customer Type",

    'summary': """
        ABK Customer Type""",

    'description': """
        ABK Customer Type
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Customizations',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/agent_name_views.xml',
        'views/views.xml',
    ],
}
