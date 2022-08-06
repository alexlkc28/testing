# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderCustom(models.Model):
    _inherit = 'purchase.order'

    customer_id = fields.Many2one('res.partner', 'Customer Name')
    customer_number = fields.Char(related='customer_id.customer_no', string='Customer Number')
    customer_phone = fields.Char(related='customer_id.phone', string='Customer Telephone Number')

    sale_order_list = fields.One2many('sale.order', 'po_id', string='Sales', compute="_compute_so_list")
    so_id = fields.Many2one('sale.order', string='Sale Order')

    vendor_number = fields.Char(related='partner_id.customer_no', string='Vendor Number')
    vendor_phone = fields.Char(related='partner_id.phone', string='Vendor Telephone Number')

    @api.onchange('customer_id')
    def _compute_so_customer_id(self):
        for record in self:
            record['sale_order_list'] = record.env['sale.order'].search([('partner_id', '=', record.customer_id.id)])

    def _compute_so_list(self):
        for record in self:
            record['sale_order_list'] = record.env['sale.order'].search([('partner_id', '=', record.customer_id.id)])


class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'
    po_id = fields.Many2one('purchase.order', string='Purchase')
    purchase_order_list = fields.One2many('purchase.order', 'so_id', string='Purchase Orders',
                                          compute="_compute_po_list")
    customer_number = fields.Char(related='partner_id.customer_no', string='Customer ID')

    def _compute_po_list(self):
        for record in self:
            record['purchase_order_list'] = record.env['purchase.order'].search(
                [('partner_id', '=', record.partner_id.id)])

    @api.onchange('partner_id')
    def _compute_po_partner_id(self):
        for record in self:
            record['purchase_order_list'] = record.env['purchase.order'].search(
                [('partner_id', '=', record.partner_id.id)])


class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'

    sequence = fields.Integer(compute='_compute_item_sequence', store=True, readonly=True)

    @api.depends('sequence', 'order_id')
    def _compute_item_sequence(self):
        for record in self:
            for order in record.mapped('order_id'):
                number = 1
                for line in order.order_line:
                    line.sequence = number
                    number += 1

    @api.onchange('product_id')
    def product_id_change(self):
        for record in self:
            for order in record.mapped('order_id'):
                number = 0
                for line in order.order_line:
                    line.sequence = number
                    number += 1

        return super().product_id_change()


class PurchaseOrderLineCustom(models.Model):
    _inherit = 'purchase.order.line'

    sequence = fields.Integer(compute='_compute_item_sequence', store=True, readonly=True)

    @api.depends('sequence', 'order_id')
    def _compute_item_sequence(self):
        for record in self:
            for order in record.mapped('order_id'):
                number = 1
                for line in order.order_line:
                    line.sequence = number
                    number += 1

    @api.onchange('product_id')
    def product_id_change(self):
        for record in self:
            for order in record.mapped('order_id'):
                number = 0
                for line in order.order_line:
                    line.sequence = number
                    number += 1
