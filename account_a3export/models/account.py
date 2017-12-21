# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    a3_sync = fields.Boolean(default=False, copy=False)
    dua_document_number = fields.Char()
    operation_date = fields.Date(compute='_compute_operation_date')

    def _compute_operation_date(self):
        for invoice in self:
            if 'refund' in invoice.type:
                invoice.operation_date = invoice.refund_invoice_ids and \
                    invoice.refund_invoice_ids[0].date_invoice or ''
            else:
                invoice.operation_date = invoice.date_invoice


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    def a3_get_tax(self):
        # TODO: Eliminar codigo duplicado?
        self.ensure_one()
        tax_codes = ['S_IVA21B', 'S_IVA4B', 'S_IVA_NS', 'S_IVA10B',
                     'S_IVA0_IC', 'S_IVA0_E']
        tax = self.invoice_line_tax_ids.filtered(lambda r: r.description in
                                                 tax_codes)
        if tax:
            currency = self.invoice_id and self.invoice_id.currency_id or None
            price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
            taxes = tax.compute_all(price, currency, self.quantity,
                                    product=self.product_id,
                                    partner=self.invoice_id.partner_id)
            return (tax.amount, taxes['taxes'][0]['amount'])
        else:
            return (0, 0)

    def a3_get_surcharge(self):
        self.ensure_one()
        surcharge_codes = ['S_REQ05', 'S_REQ014', 'S_REQ52']
        tax = self.invoice_line_tax_ids.filtered(lambda r: r.description in
                                                 surcharge_codes)
        if tax:
            currency = self.invoice_id and self.invoice_id.currency_id or None
            price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
            taxes = tax.compute_all(price, currency, self.quantity,
                                    product=self.product_id,
                                    partner=self.invoice_id.partner_id)
            return (tax.amount, taxes['taxes'][0]['amount'])
        else:
            return (0, 0)

    def a3_get_irpf(self):
        self.ensure_one()
        tax = self.invoice_line_tax_ids.filtered(
            lambda r: 'IRPF' in r.description)
        if tax:
            currency = self.invoice_id and self.invoice_id.currency_id or None
            price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
            taxes = tax.compute_all(price, currency, self.quantity,
                                    product=self.product_id,
                                    partner=self.invoice_id.partner_id)
            return (tax.amount, taxes['taxes'][0]['amount'])
        else:
            return (0, 0)


class AccountFiscalPosition(models.Model):

    _inherit = 'account.fiscal.position'

    a3_code = fields.Char(length=2)


class AccountMove(models.Model):

    _inherit = 'account.move'

    a3_sync = fields.Boolean(copy=False)


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    line_type = fields.Char(compute='_compute_line_type')
    amount = fields.Float(compute='_compute_line_type')

    def _compute_line_type(self):
        for line in self:
            if line.debit:
                line.line_type = 'D'
                line.amount = line.debit
            elif line.credit:
                line.line_type = 'H'
                line.amount = line.credit
