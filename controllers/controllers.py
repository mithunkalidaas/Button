# -*- coding: utf-8 -*-
from odoo import http


class Button(http.Controller):
    @http.route('/button/button/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/button/button/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('button.listing', {
            'root': '/button/button',
            'objects': http.request.env['button.button'].search([]),
        })

    @http.route('/button/button/objects/<model("button.button"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('button.object', {
            'object': obj
        })
