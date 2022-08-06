from odoo import models, fields, api


class PurchaseOrderCustom(models.Model):
    _inherit = 'purchase.order'

    abk_productno = fields.Char('Product Number')
    abk_podate = fields.Datetime('Order Date', default=fields.Datetime.now)
    abk_effective_date = fields.Datetime('Effective Date', default=fields.Datetime.now)
    abk_salescode = fields.Char('Sales Code')
    abk_pono = fields.Char('Order Number')
    abk_expdeldate = fields.Datetime('Expected delivery date')
    abk_promised_date = fields.Datetime('Promised Date')
    abk_otcharge = fields.Char('Over Time Charge')
    abk_process = fields.Char('Process')
    abk_yard = fields.Char('Yard')
    abk_content = fields.Char('Content')
    abk_productype = fields.Char('Material Type')
    abk_brand = fields.Many2one("abk.brand", string='Brand')
    abk_remark2 = fields.Text('Remark')
    abk_telephone = fields.Char('Telephone')
    abk_jobno = fields.Char('Job Number')
    abk_amendment = fields.Char('Amendement')
    abk_amenduser = fields.Char('Amendement User')
    abk_amenddate = fields.Datetime('Amendement Date')

    abk_produser = fields.Char('Production User')
    abk_stockqty = fields.Float('Stock quantity')
    abk_poqty = fields.Float('PO Quantity')
    abk_pounit = fields.Many2one('uom.uom', string='PO Unit')

    abk_delmark = fields.Text('Delivery Mark')
    abk_internalcode = fields.Char('Internal Code')
    abk_deladdress = fields.Text('Delivery Address')
    abk_receivequantity = fields.Float('Receive quantity')
    abk_not_yet_receive_quantity = fields.Char('Not yet receive quantity')
    abk_worksorder_number = fields.Char('Worksorder number')
    abk_tax = fields.Char('Tax')
    abk_potype = fields.Char('PO Type')
    abk_unitprice = fields.Monetary('Unit price')
    abk_extracost = fields.Monetary('Extra Cost')
    abk_materialduedate = fields.Datetime('Material Due Date')
    abk_sono = fields.Char('Sales order number')
    abk_sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    abk_promised_date = fields.Datetime('Promised Date')
    abk_amendement_user = fields.Many2one("res.users", string='Amendement User')
    abk_amendement_date_time = fields.Datetime('Amendement Date')
    abk_reclocation = fields.Char('reclocation')
    abk_attention = fields.Char('Attention')
    abk_status = fields.Char('ABK Status')
    abk_payterm = fields.Char('Payterm')
    abk_paydesc = fields.Text('Payterm Description')
    abk_delterm = fields.Char('Delivery Term')
    abk_exrate = fields.Char('Exrate')
    abk_amount = fields.Float('ABK Amount')
    abk_otheramt = fields.Float('ABK Otheramt')
    abk_gtotal = fields.Float('ABK gtotal')
    abk_packrmk = fields.Text('packrmk')
    abk_other_charges = fields.Float('Charge')
    abk_warehouse = fields.Many2one('stock.warehouse', string='Warehouse')
    abk_ship_via = fields.Selection([
        ('option 1', 'Option 1'),
        ('option 2', 'Option 2'),
        ('option 3', 'Option 3')
    ], string='Ship Via', readonly=False, default='')
    abk_purchase_usage_type = fields.Selection([
        ('Maintenance', 'Maintenance')
    ], string='Purchase Usage Type', readonly=False, default='')

    # state = fields.Selection([
    #     ('draft', 'RFQ'),
    #     ('sent', 'RFQ Sent'),
    #     ('to approve', 'To Approve'),
    #     ('purchase', 'Purchase Order'),
    #     ('done', 'Locked'),
    #     ('cancel', 'Cancelled')
    # ], string='Status', readonly=False, index=True, copy=False, default='draft', tracking=True)

    # READONLY_STATES = {
    #     'purchase': [('readonly', True)],
    #     'done': [('readonly', True)],
    #     'cancel': [('readonly', True)],
    # }
    #
    # partner_id = fields.Many2one('res.partner', string='Vendor', required=False, states=READONLY_STATES,
    #                              change_default=True, tracking=True,
    #                              domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    #                              help="You can find a vendor by its Name, TIN, Email or Internal Reference.")


class PurchaseOrderLineCustom(models.Model):
    _inherit = 'purchase.order.line'

    abk_impt = fields.Char('Tax Type')
    abk_impt_1 = fields.Char('Tax Type')
    abk_size = fields.Char('Size')
    abk_actqty = fields.Float('Actual quantity')
    abk_fcolour = fields.Char('fcolour')
    abk_bcolour = fields.Char('bcolour')
    abk_chcolour = fields.Char('chcolour')
    abk_fcolourno = fields.Char('fcolourno')
    abk_bcolourno = fields.Char('bcolourno')
    abk_machine = fields.Char('Machine')
    abk_paper = fields.Char('Paper')
    abk_actual_quantity = fields.Integer("Actual Quantity")
    abk_tax_type = fields.Char("Tax Type")
    abk_ounitpce = fields.Float("ounitpce")
    abk_discnt = fields.Float("discnt")
    abk_expdeldate = fields.Datetime("Expdeldate")
    abk_poend = fields.Boolean("poend")
    abk_remark = fields.Text("Remark")
    abk_buycompany = fields.Char("Buy company")
    abk_paylocation = fields.Char("pay Location")
    abk_venitem = fields.Char("Venitem")
    abk_recqty = fields.Float("recqty")
    abk_recunit = fields.Char("recunit")
