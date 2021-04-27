# -*- coding: utf-8 -*-

from odoo import models, fields, api


class button(models.Model):
    _name = 'button.button'
    _description = 'button.button'

    name = fields.Char()
    state = fields.Char(default='Draft')
    date = fields.Date(default=fields.Date.today, readonly=True)

    def con(self):
        self.state='CONFIRM'