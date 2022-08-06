# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    combined_so = fields.Boolean(default=False)

    def action_merged_proforma_invoice(self):
        """ merged proforma invoice"""
        self.env['sale.order'].sudo().create({
            'partner_id': self.partner_id.id,
            'pricelist_id': self.pricelist_id.id,
            'combined_so': True,
            'created_by': self.env.user.id,
            'order_line': self.order_line.ids
        })
