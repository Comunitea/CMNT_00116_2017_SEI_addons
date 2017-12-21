# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models
from datetime import date


class ExportA3Wizard(models.TransientModel):

    _name = 'export.a3.wizard'

    def export(self):
        self.ensure_one()

        data = {'name': date.today()}
        data['partners'] = [(6, 0, self.env['res.partner'].search(
            [('a3_sync', '=', False)]).ids)]
        data['invoices'] = [(6, 0, self.env['account.invoice'].search(
            [('a3_sync', '=', False), ('state', 'in', ['open', 'paid'])]).ids)]
        data['moves'] = [(6, 0, self.env['account.move'].search(
            [('a3_sync', '=', False),
             ('line_ids.invoice_id', '=', False)]).ids)]
        if not data['partners'][0][2] and not data['invoices'][0][2] and not \
                data['moves'][0][2]:
            return

        exportation = self.env['a3.exportation'].create(data)
        exportation.create_file()

        exportation.partners.write({'a3_sync': True})
        exportation.invoices.write({'a3_sync': True})
        exportation.moves.write({'a3_sync': True})

        action = self.env.ref(
            'account_a3export.a3_exportation_action').read()[0]
        action['res_id'] = exportation.id
        action['views'] = [(self.env.ref(
            'account_a3export.a3_exportation_view_form').id, 'form')]
        return action
