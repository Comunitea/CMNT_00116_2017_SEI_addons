# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Custom modification for Seistag',
    'summary': '',
    'version': '11.0.1.0.0',
    'category': 'Uncategorized',
    'website': 'comunitea.com',
    'author': 'Comunitea',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base',
        'sale',
        'purchase'
    ],
    'data': [
        'views/harbour.xml',
        'views/sale_view.xml',
        'views/purchase_view.xml',
        'security/ir.model.access.csv'
    ],
}
