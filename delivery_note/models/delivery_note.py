from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_merged_so_only(self):

        delivery_ids = self.env["stock.picking"].search(
            [("sale_id", 'in', self.ids)]).ids

        if delivery_ids:
            return {
                'name': 'Order',
                'res_model': 'stock.picking',
                'type': 'ir.actions.act_window',
                'domain': [('id', 'in', delivery_ids)],
                'view_mode': 'list,form',
                'view_type': 'list',
                'target': 'current'
            }

    def _compute_picking_ids(self):

        for order in self:
            order.delivery_count = len(order.picking_ids)

