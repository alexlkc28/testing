# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class DmrProcess(models.Model):
    """dmr process"""
    _name = "dmr.process"
    _description = "DMR Process"
    _rec_name = "purchase_order_id"

    partner_id = fields.Many2one('res.partner', string='Vendor')
    dmr_line_ids = fields.One2many(
        'dmr.order.line', 'dmr_process_id', string='Lines')
    purchase_order_id = fields.Many2one('purchase.order')
    date_approve = fields.Datetime(string='Confirmation Date')
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('completed', 'Completed')],
        help="state is used to separate Draft,Completed",
        default='draft')

    def button_validate(self):
        """button validate"""
        for invoice in self.purchase_order_id.invoice_ids:
            action = self.env["ir.actions.actions"]._for_xml_id(
                "account.action_view_account_move_reversal")

            if all(invoice.move_type == 'in_invoice'
                   for invoice in self.purchase_order_id.invoice_ids):
                action['name'] = _('Debit Note')

            action['context'] = (
                {'dmr_mov_ids': self.purchase_order_id.invoice_ids.ids})
            self.state = 'completed'
            return action


class DmrOrderLine(models.Model):
    """dmr order line"""
    _name = 'dmr.order.line'
    _description = "DMR Order Lines"

    product_id = fields.Many2one('product.product', string='Product')
    dmr_process_id = fields.Many2one('dmr.process', string='DMR Process')
    description = fields.Text(string='Description')
    quantity_product_uom = fields.Float(string='Quantity')
    received_qty = fields.Float(string='Received')
    invoiced_qty = fields.Float(string='Billed')
    unit_price = fields.Float(string='Unit Price')
    tax_id = fields.Many2many('account.tax', string='Taxes')
    sub_total = fields.Monetary(string='Sub Total')
    currency_id = fields.Many2one(
        'res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company.id)


class PurchaseOrder(models.Model):
    """purchase order"""
    _inherit = 'purchase.order'
    dmr_process_id = fields.Many2one('dmr.process')

    def dmr_button(self):

        if self.order_line.filtered(lambda line: not line.dmr_line_id):
            dmr = self.env['dmr.process'].sudo().create({
                'partner_id': self.partner_id.id,
                'date_approve': self.date_approve,
                'purchase_order_id': self.id

            })
            self.dmr_process_id = dmr.id
        else:
            dmr = self.dmr_process_id
        for line in self.order_line:
            if not line.dmr_line_id:
                dmr_process = self.env['dmr.order.line'].sudo().create({
                    'product_id': line.product_id.id,
                    'description': line.name,
                    'quantity_product_uom': line.product_uom_qty,
                    'received_qty': line.qty_received,
                    'invoiced_qty': line.qty_invoiced,
                    'unit_price': line.price_unit,
                    'tax_id': line.taxes_id.ids,
                    'sub_total': line.price_subtotal,
                    'dmr_process_id': dmr.id

                })
                line.dmr_line_id = dmr_process.id

    def get_dmr(self):
        """get dmr"""
        view = self.env.ref('dmr_process.dmr_process_views_form')
        return {
            'name': _('DMR'),
            'res_model': 'dmr.process',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', self.env['dmr.process'].search(
                [('purchase_order_id', '=', self.id)]).ids)],
            'target': 'current',
        }


class PurchaseOrderLine(models.Model):
    """purchase order line"""
    _inherit = 'purchase.order.line'
    dmr_line_id = fields.Many2one('purchase.order.line')


class AccountMoveReversal(models.TransientModel):
    """account move reversal"""
    _inherit = 'account.move.reversal'

    @api.model
    def default_get(self, fields):
        """default get"""
        res = super(AccountMoveReversal, self).default_get(fields)
        if self.env.context.get('active_model') == 'dmr.process':
            move_ids = self.env['account.move'].browse(
                self.env.context['dmr_mov_ids'])
            if 'move_ids' in fields:
                res['move_ids'] = [(6, 0, move_ids.ids)]
        res
        return res
