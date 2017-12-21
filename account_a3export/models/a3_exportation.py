# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from ..tools import A3_jinja
from openerp import models, fields
import base64


class A3Exportation(models.Model):

    _name = 'a3.exportation'

    name = fields.Date('Date')
    exported_file = fields.Binary(attachment=True)
    file_name = fields.Char(compute='_compute_file_name')
    partners = fields.Many2many('res.partner')
    invoices = fields.Many2many('account.invoice')
    moves = fields.Many2many('account.move')

    def _compute_file_name(self):
        for exportation in self:
            exportation.file_name = '%s.txt' % \
                exportation.name.replace('-', '')

    def create_file(self):
        self.ensure_one()
        env = A3_jinja._get_env()

        template = env.get_template('partner')
        template.globals['partners'] = self.partners
        data = template.render()

        template = env.get_template('invoice')
        template.globals['soportado'] = self.env.ref(
            'l10n_es.1_account_common_472')
        template.globals['repercutido'] = self.env.ref(
            'l10n_es.1_account_common_477')
        template.globals['retencion'] = self.env.ref(
            'l10n_es.1_account_common_4751')
        template.globals['invoices'] = self.invoices
        data += template.render()

        template = env.get_template('account_move')
        template.globals['moves'] = self.moves
        data += template.render()

        self.exported_file = base64.encodestring(bytes(data, 'utf-8'))
