# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    document_address = fields.Char(compute='_compute_document_address')

    def _compute_document_address(self):
        for partner in self:
            address = ''
            if partner.street:
                address += partner.street
            if partner.street2:
                address += ' {}'.format(partner.street2)
            if partner.city:
                address += ', {}'.format(partner.city)
            if partner.zip:
                address += ', {}'.format(partner.zip)
            if partner.state_id.name:
                address += ', {}'.format(partner.state_id.name)
            if partner.country_id.name:
                address += ', {}'.format(partner.country_id.name)
            partner.document_address = address


class ResBank(models.Model):
    _inherit = 'res.bank'

    document_address = fields.Char(compute='_compute_document_address')

    def _compute_document_address(self):
        for partner in self:
            address = ''
            if partner.street:
                address += partner.street
            if partner.street2:
                address += ' {}'.format(partner.street2)
            if partner.city:
                address += ', {}'.format(partner.city)
            if partner.zip:
                address += ', {}'.format(partner.zip)
            if partner.state.name:
                address += ', {}'.format(partner.state.name)
            if partner.country.name:
                address += ', {}'.format(partner.country.name)
            partner.document_address = address
