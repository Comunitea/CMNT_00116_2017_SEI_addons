# © 2018 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

class SeistagHarbour(models.Model):
    _name = 'seistag.harbour'

    name = fields.Char(string='Name', required=True, copy=False)
