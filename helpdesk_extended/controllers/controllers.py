# -*- coding: utf-8 -*-
# from odoo import http


# class HelpDeskExtended(http.Controller):
#     @http.route('/help_desk_extended/help_desk_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/help_desk_extended/help_desk_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('help_desk_extended.listing', {
#             'root': '/help_desk_extended/help_desk_extended',
#             'objects': http.request.env['help_desk_extended.help_desk_extended'].search([]),
#         })

#     @http.route('/help_desk_extended/help_desk_extended/objects/<model("help_desk_extended.help_desk_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('help_desk_extended.object', {
#             'object': obj
#         })
