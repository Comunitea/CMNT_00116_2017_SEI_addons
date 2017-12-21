# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from jinja2 import Environment, PackageLoader
from odoo.tools import float_repr, float_round, DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from datetime import datetime, date


class A3_jinja(object):

    @staticmethod
    def __l(value, size, filling=' '):
        if isinstance(value, bool):
            value = ''
        return value[:size].ljust(size, filling)

    @staticmethod
    def __r(value, size, filling='0'):
        if isinstance(value, bool):
            value = ''
        return value[:size].rjust(size, filling)

    @staticmethod
    def __a3_float(value, size=14, symbol=True):
        # +000000.00
        # 00.00
        size_without_symbol = size
        if symbol:
            size_without_symbol -= 1
        format_value = A3_jinja.__r(float_repr(float_round(value, precision_digits=size), precision_digits=2), size_without_symbol)
        if symbol:
            format_value = '+' + format_value
        return format_value

    @staticmethod
    def __a3_date(value):
        if not value:
            return ''
        value = value[:10]
        return datetime.strptime(value, DATE_FORMAT).strftime('%Y%m%d')

    @staticmethod
    def _get_env():
            env = Environment(loader=PackageLoader('odoo.addons.account_a3export', 'templates'))
            env.filters['l'] = A3_jinja.__l
            env.filters['r'] = A3_jinja.__r
            env.filters['a3_float'] = A3_jinja.__a3_float
            env.filters['a3_date'] = A3_jinja.__a3_date
            env.globals['today'] = date.today().strftime('%Y-%m-%d')
            return env
