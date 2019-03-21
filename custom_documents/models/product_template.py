# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'


    length = fields.Float(string="Length")
    width = fields.Float(string="Width")
    thick = fields.Float(string="Thick")
