# -*- coding: utf-8 -*-
{
    'name': "phidias_fix_pos_fiscal_position",

    'summary': """
        Fix problem calculation tax when tax is include in price and change fiscal position in POS
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Phidias",
    'website': "http://www.phidias.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'views/assets.xml',
    ],
}
