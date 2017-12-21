# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'a3 exportation',
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
        'base_partner_sequence',
        'account',
        'account_invoice_refund_link'
    ],
    'data': [
        'wizard/export_a3.xml',
        'views/a3_exportation.xml',
        'views/account.xml',
        'security/ir.model.access.csv'
    ],
}
