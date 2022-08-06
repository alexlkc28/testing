from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    number = fields.Integer(string='Sl. No.', compute='_compute_serial_number', store=True)

    @api.depends('sequence', 'order_id')
    def _compute_serial_number(self):
        for order_line in self:
            if not order_line.number:
                serial_no = 1
                for line in order_line.mapped('order_id').order_line:
                    line.number = serial_no
                    serial_no += 1