# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class custom_sale_order(models.Model):
    _inherit = 'sale.order'

    paid = fields.Float('Paid', compute="depends_invoice_id")
    remaining = fields.Integer('Remaining')
    payment_schedule = fields.Selection(
        [('late', 'Late'), ('not_late', 'Not late')], string="Payment Schedule")
    can_deliver = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                   string="Can deliver")
    count_paid = fields.Many2many("account.move", string='Count Paid')

    abk_purchase_order_number = fields.Integer('Purchase Order Number')
    abk_purchase_order_date = fields.Datetime('Purchase Order Date')
    # abk_customer_purchase_order = fields.Char(related="po_id.customer_id",string='Customer Purchase Order')
    abk_sales_code = fields.Char('Sales Code')
    abk_payment_description = fields.Text('Payment Description')
    abk_attention = fields.Many2one("res.partner", string='Attention')
    abk_remark = fields.Char('Remark')
    abk_user_id = fields.Many2one("res.users", string='User ID')
    abk_amendement_user = fields.Many2one("res.users", string='Amendement User')
    abk_amendement_date_time = fields.Datetime('Amendement Date')
    abk_po_void = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                   string="PO Void")
    abk_po_valid = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                    string="PO Valid")
    abk_sales_date = fields.Datetime('Sales Date',
                                     default=lambda self: fields.Datetime.now())
    abk_salesperson = fields.Many2one("res.users", string='Saleperson')
    abk_salesperson_name = fields.Many2one("res.users",
                                           string='Saleperson Name')
    abk_sales_team = fields.Many2one("crm.team", string='Sale Team')
    abk_sales_order_type = fields.Char('Sales Order Type')
    abk_sales_order_number = fields.Char('Sales Order number')
    abk_project = fields.Char('Project')
    abk_product_number = fields.Integer('Product number')
    abk_product_description = fields.Text('Product description')
    abk_order_quantity = fields.Integer('Order Quantity')
    abk_unit = fields.Integer('Unit')
    abk_order_currency = fields.Many2one(related="partner_id.currency",
                                         string="Order Currency",
                                         readonly=False)
    abk_require_date = fields.Datetime('Require date')
    abk_delivery_address = fields.Text('Delivery address')
    abk_delivery_description = fields.Text('Delivery Description')
    abk_proforma_invoice_remark = fields.Text('Proforma Invoice Remark')
    abk_co_remark = fields.Char('CO Remark')
    abk_customer_remark = fields.Char('Customer Remark')
    abk_po_number = fields.Char('PO number')
    abk_status = fields.Char('Customer Status')
    abk_direct_manufacturing = fields.Char('Direct manufacturing')
    abk_brand = fields.Many2one("abk.brand", string='Brand')
    abk_product_importance = fields.Char('Product importance')
    abk_po_project = fields.Char('PO project')
    abk_delivery_date = fields.Datetime('Delivery date')
    abk_customer_short_form = fields.Char('Customer short form')
    abk_sub_brand = fields.Many2one("abk.brand", string='Sub-Brand')
    abk_salesman = fields.Char('Salesman')
    abk_sortkey1 = fields.Char('Sortkey1')
    abk_agent = fields.Many2one("res.partner",
                                domain=lambda self:[('abk_customer_type', '=', self.env.ref(
                                    'abk_customer_type.abk_agent_type_view_list').id)],
                                string='Agent')
    abk_agent_type = fields.Selection(string='Agent Type',
                                      related="abk_agent.company_type"
                                      )

    abk_web_order_number = fields.Char('Web Order Number')
    abk_format_id = fields.Integer('Format ID')
    abk_customer_service_person = fields.Many2one('hr.employee',
                                                  string='Customer Service Person')
    abk_referrer = fields.Char('Referrer')
    abk_proforma_invoice_number = fields.Integer('Proforma Invoice Number')
    abk_podate = fields.Datetime('PO Date')
    abk_pono = fields.Char('PO No')
    abk_custpono = fields.Char('Customer PO Number')
    abk_input_date_time = fields.Datetime('Input Date')
    abk_conprn = fields.Char('Con Prn')
    abk_condate_time = fields.Datetime('Con Date')
    abk_ename = fields.Char('English Name')
    abk_order_date = fields.Datetime('Order Date',
                                     default=lambda self: fields.Datetime.now())
    abk_customer_english_name = fields.Char(related='partner_id.name_english',
                                            string='Customer English Name')
    abk_epicord = fields.Char("EPICOR")
    abk_premain = fields.Integer("Premain")
    abk_comremain = fields.Integer("Comremain")
    abk_dremain = fields.Integer("Dremain")
    abk_iremain = fields.Integer("Iremain")
    abk_expdeldate = fields.Datetime("Expdeldate")
    abk_prevpono = fields.Char("Prevpono")
    abk_yard = fields.Float("Yard")
    abk_content = fields.Char("Content")
    abk_productype = fields.Char("Productype")
    abk_edgetype = fields.Char("Edgetype")
    abk_type1 = fields.Boolean("type1")
    abk_type2 = fields.Boolean("type2")
    abk_type3 = fields.Boolean("type3")
    abk_type4 = fields.Boolean("type4")
    abk_type5 = fields.Boolean("type5")
    abk_hs_code = fields.Many2one("abk.hscommodity", string="HS Code")
    abk_lotno = fields.Boolean("lotno")
    abk_otcharge = fields.Boolean("otcharge")
    abk_foccbx = fields.Boolean("foccbx")
    abk_focdesc = fields.Boolean("focdesc")
    abk_stkcbx = fields.Boolean("stkcbx")
    abk_stkrb = fields.Char("stkrb")
    abk_samcbx = fields.Boolean("samcbx")
    abk_samst = fields.Boolean("samst")
    abk_con_status = fields.Boolean("con status")
    abk_fsc_claim = fields.Many2one("abk.fscclaim", string='FSC Claim')
    wos_address_id = fields.Selection([
        ('1', 'Invoice Address'),
        ('2', 'Delivery Address'),
        ('3', 'Other Address'),
        ('4', 'Private Address')], string="WOS Address ID")

    # state = fields.Selection([
    #     ('draft', 'Quotation'),
    #     ('sent', 'Quotation Sent'),
    #     ('sale', 'Sales Order'),
    #     ('done', 'Locked'),
    #     ('cancel', 'Cancelled'),
    # ], string='Status', readonly=False, copy=False, index=True, tracking=3, default='draft')
    #
    # name = fields.Char(string='Order Reference', required=False, copy=False, readonly=False,
    #                    states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))

    @api.depends('invoice_ids')
    def depends_invoice_id(self):
        for invoice in self:
            amount_due = 0.0
            if invoice:
                for aml in invoice.invoice_ids:
                    amount_due += (aml.amount_total - aml.amount_residual)
            invoice.update({
                'paid': amount_due
            })

    @api.model
    def get_currency(self):
        """function to get currency"""
        default = self.env.ref("contacts").currency
        return default

    def action_confirm(self):
        res = super(custom_sale_order, self).action_confirm()
        self.get_contact_data()
        return res

    def get_contact_data(self):
        count = 0
        wos_address = ''
        wos_address_id = self.wos_address_id

        if wos_address_id:
            if wos_address_id == '1':
                wos_address = 'invoice'
            elif wos_address_id == '2':
                wos_address = 'delivery'
            elif wos_address_id == '3':
                wos_address = 'other'
            elif wos_address_id == '4':
                wos_address = 'private'

            for item in self.partner_id.child_ids:
                if item.type == wos_address:
                    count += 1

            if count == 0:
                raise UserError("Missing Address Type in selected Customer!")


class CustomSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    abk_material_type = fields.Char('Material Type')
    abk_item_size = fields.Char('Item size')
    abk_outsourcing = fields.Char('Outsourcing')
    abk_hka_amount = fields.Float(string='HKA Amount')
    abk_currency = fields.Text(string="Currency")
    abk_symbol = fields.Text(string="Symbol")
    abk_rate = fields.Float(string="Rate")
    abk_amount = fields.Float(string="Amount")
    abk_output_quantity = fields.Integer(string='Output Quantity')
    abk_ft = fields.Char(string='FT(USD)')
    abk_ct = fields.Char(string='CT(USD)')
    abk_hkd_amount = fields.Float(string='Amount(HKD)')
    abk_web_line_item = fields.Char(string='Web Order Line Item')
    abk_art_work_no_pages = fields.Char(string='Art Work Pages')
    abk_art_work_size = fields.Char(string='Art Work Size')
    abk_group = fields.Char(string='Group')
    abk_customer_material_no = fields.Char(related='product_id.abk_material_no',
                                           string="Customer Material Number")
    abk_product_no = fields.Char(related='product_id.default_code')
    abk_fcolour = fields.Char("fcolour")
    abk_bcolour = fields.Char("bcolour")
    abk_fcolourno = fields.Integer('fcolourno')
    abk_bcolourno = fields.Integer('bcolourno')
    abk_chcolour = fields.Char("chcolour")
    abk_machine = fields.Char("machine")
    abk_paper = fields.Char("paper")
    abk_process = fields.Char("process")
    abk_impt = fields.Char(string='Tax Type')
    abk_lotno = fields.Boolean("lotno")
    abk_premain = fields.Integer("premain")
    abk_comremain = fields.Integer("comremain")
    abk_dremain = fields.Integer("dremain")
    abk_iremain = fields.Integer("iremain")
    abk_expdeldate = fields.Datetime('expdeldate')
    abk_otcharge = fields.Boolean("otcharge")
    abk_foccbx = fields.Boolean("foccbx")
    abk_focdesc = fields.Char("focdesc")
    abk_stkcbx = fields.Boolean("stkcbx")
    abk_stkrb = fields.Char("stkrb")
    abk_samcbx = fields.Char("samcbx")
    abk_samst = fields.Char("samst")
    abk_prevpono = fields.Char("prevpono")
    abk_con_status = fields.Boolean("constatus")
    abk_hs_code = fields.Many2one("abk.hscommodity", string="HS Code")
    abk_unitpce = fields.Char("Unit pce")


class warning_delivery(models.Model):
    _inherit = 'stock.picking'
    delivery_warning = fields.Boolean('Delivery Warning',
                                      compute="compute_delivery_warning")

    def compute_delivery_warning(self):
        for record in self:
            record['delivery_warning'] = record.sale_id.is_warning
