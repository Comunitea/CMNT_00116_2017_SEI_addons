# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ResPartner(models.Model):

    _inherit = 'res.partner'

    a3_sync = fields.Boolean(default=False, copy=False)
    a3_account = fields.Char(compute='_compute_a3_account')
    a3_vat = fields.Char(compute='_compute_a3_vat')

    def _get_customer_account(self, account):
        self.ensure_one()
        return '%s%s' % (account.code, self.ref or '')

    def _compute_a3_account(self):
        for partner in self:
            if partner.customer:
                partner.a3_account = partner._get_customer_account(
                    partner.property_account_receivable_id)
            if partner.supplier:
                partner.a3_account = partner._get_customer_account(
                    partner.property_account_payable_id)

    def _compute_a3_vat(self):
        for partner in self:
            formated_vat = ''
            if partner.vat:
                if "ES" in partner.vat:
                    formated_vat = partner.vat.replace('ES', '')
                else:
                    formated_vat = partner.vat
            partner.a3_vat = formated_vat

    def write(self, vals):
        if vals.get('ref', False) or vals.get('name', False) or \
                vals.get('vat', False) or vals.get('street', False) or \
                vals.get('phone', False) or vals.get('mobile', False) or \
                vals.get('active', False):
            vals['a3_sync'] = False
        return super(ResPartner, self).write(vals)
