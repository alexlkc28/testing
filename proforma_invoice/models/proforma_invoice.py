# -*- coding: utf-8 -*-

from odoo import fields, models


class ProformaInvoice(models.Model):
    _name = 'proforma.invoice'
    _description = 'Proforma Invoice'

    sale_order_ids = fields.Many2many('sale.order')
