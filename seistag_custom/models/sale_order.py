# © 2018 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class SaleOrderUnitType(models.Model):

    _name = 'sale.order.unit.type'

    name = fields.Char(required=True)


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    harbour_id = fields.Many2one('seistag.harbour', string='Harbour')
    unit_type_id = fields.Many2one('sale.order.unit.type', 'Unit types')
