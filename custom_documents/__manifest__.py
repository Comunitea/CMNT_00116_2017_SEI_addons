# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Document customizations',
    'version': '11.0.1.0.0',
    'author': 'Comunitea',
    'website': 'www.comunitea.com',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'sale_stock'
    ],
    'data': [
        'views/report_templates.xml',
        'views/report_sale_order.xml',
        'data/report_paperformat.xml'
    ],
    'installable': True,
}
