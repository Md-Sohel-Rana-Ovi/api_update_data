# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json


class ApiUpdateData(http.Controller):
    @http.route('/', auth='public',website=True)
    def index(self, **kw):
        return request.render('api_update_data.api_data_update_form', {})


#     @http.route('/api_update_data/api_update_data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('api_update_data.listing', {
#             'root': '/api_update_data/api_update_data',
#             'objects': http.request.env['api_update_data.api_update_data'].search([]),
#         })

#     @http.route('/api_update_data/api_update_data/objects/<model("api_update_data.api_update_data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('api_update_data.object', {
#             'object': obj
#         })
