from odoo import models, fields, api


class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    abk_ium = fields.Many2one('uom.uom', string='Inventory UoM')
    abk_so_uom_id = fields.Many2one('uom.uom', string='Sale UoM')
    abk_class_id = fields.Many2one("abk.product.class", string='Product Class')
    abk_commodity_code = fields.Many2one("abk.hscommodity", string='HS Code')
    abk_brand = fields.Many2one("abk.brand", string='Brand')
    abk_sub_brand = fields.Many2one("abk.brand", string='Sub-Brand')
    abk_grs_weight = fields.Float('GRS Weight(g)')
    abk_fsc_paper_weight = fields.Char('FSC Paper Weight (kg)')
    abk_fsc_claim = fields.Many2one("abk.fscclaim",string='FSC Claim')
    abk_agent = fields.Many2one("res.partner", string='Agent')
    abk_format_id = fields.Integer('Format ID')
    abk_wo_salesman = fields.Many2one("res.users", string='WO Salesman')
    abk_part_description = fields.Text('Product Description')
    abk_item_size = fields.Char('Item Size')
    abk_internal_price = fields.Monetary(string="Internal Price")
    abk_tax_category = fields.Char(string="TaxCloud Category")
    abk_co_created = fields.Boolean(string="CO Created")
    abk_manufacturer = fields.Many2one("mrp.production", string="Manufacturer")
    abk_country_of_origin = fields.Many2one('res.country', string='Country of Origin')
    abk_supp_unit_factor = fields.Float(string="Supplier Units Factor")
    abk_partial_completed = fields.Char(string="Partial Completed")
    abk_inventory = fields.Char(string="Inventory")
    abk_shelf_life_days = fields.Integer(string="Shelf Life / Days")
    abk_run_out = fields.Boolean(string="Run Out")
    abk_web_saleable = fields.Boolean(string="Web Saleable")
    abk_use_part_rev = fields.Boolean(string="Use part rev")
    abk_constrained_material = fields.Boolean(string="Constrained Material")
    abk_track_lots = fields.Boolean(string="Track Lots")
    abk_package_control_specific_uoms = fields.Boolean(string="Package Control Specific UoMs")
    abk_track_multiple_uoms = fields.Boolean(string="Track Multiple UoMs")
    abk_track_serial_numbers = fields.Boolean(string="Track Serial numbers")
    abk_consolidated_purchasing = fields.Boolean(string="Consolidated purchasing")
    abk_receipt_docs_required = fields.Boolean(string="Receipt docs Required")
    abk_shipping_docs_required = fields.Boolean(string="Shipping docs required")
    abk_link_to_contract = fields.Boolean(string="Link to contract")
    abk_mdpv = fields.Integer(string="MDPV")
    abk_returnable_container = fields.Integer(string="Returnable Container")
    abk_fk_number = fields.Char(string='F/K Number')
    abk_warranty = fields.Many2one("abk.warranty", string='Warranty')
    abk_head_asm_analysis = fields.Many2one("abk.head.analysis", string='Head/Asm analysis')
    abk_material_analysis = fields.Many2one("abk.material.analysis", string='Material Analysis')
    abk_reference_category = fields.Many2one("abk.reference.category", string='Reference Category')
    abk_rpd_part = fields.Char(string="RPD Part")
    abk_global = fields.Boolean(string="Global")
    abk_inactive = fields.Boolean(string="Inactive")
    abk_important = fields.Boolean(string="Important")
    abk_sortkey1 = fields.Char(string="SortKey1")
    abk_sortkey2 = fields.Char(string="SortKey2")
    abk_sortkey3 = fields.Char(string="SortKey3")
    abk_sortkey4 = fields.Char(string="SortKey4")
    abk_half_completed_product_inventory = fields.Boolean(string="Half completed product Inventory")
    abk_global_lock = fields.Boolean(string="Global Lock")
    abk_per_container = fields.Float(string="Per container")
    abk_sub_level_code = fields.Integer(string="Sub-Level Code")
    abk_already_open_co = fields.Boolean(string="Already open CO?")
    abk_sizew = fields.Char('Size W')
    abk_sizel = fields.Char('Size L')
    abk_sizeunit = fields.Char('Size Unit')
    abk_sizek = fields.Char('Size K')
    abk_product_no = fields.Char(string='Product No')
    abk_material_no = fields.Char(string='Customer Material No')

    abk_epicord = fields.Char("Epicor")
    abk_premain = fields.Integer("Premain")
    abk_comremain = fields.Integer("Comremain")
    abk_dremain = fields.Integer("Dremain")
    abk_iremain = fields.Integer("Iremain")
    abk_yard = fields.Float("Yard")
    abk_content = fields.Char("Content")
    abk_productype = fields.Char("Productype")
    abk_edgetype = fields.Char("Edgetype")
    abk_type1 = fields.Boolean("Type 1")
    abk_type2 = fields.Boolean("Type 2")
    abk_type3 = fields.Boolean("Type 3")
    abk_type4 = fields.Boolean("Type 4")
    abk_type5 = fields.Boolean("Type 5")
    abk_lotno = fields.Boolean("Lot no")
    abk_otcharge = fields.Boolean("Otcharge")
    abk_foccbx = fields.Boolean("Foccbx")
    abk_focdesc = fields.Boolean("Focdesc")
    abk_stkcbx = fields.Boolean("Stkcbx")
    abk_stkrb = fields.Char("stkrb")
    abk_samcbx = fields.Boolean("Samcbx")
    abk_samst = fields.Boolean("Samst")
    abk_constatus = fields.Boolean("Constatus")
    abk_fcolour = fields.Char("Fcolour")
    abk_bcolour = fields.Char("Bcolour")
    abk_fcolourno = fields.Integer('Fcolourno')
    abk_bcolourno = fields.Integer('Bcolourno')
    abk_chcolour = fields.Char("Chcolour")
    abk_machine = fields.Char("Machine")
    abk_paper = fields.Char("Paper")
    abk_process = fields.Char("Process")
    abk_sizel1 = fields.Float("Size L 1")
    abk_sizel2 = fields.Float("Size L 2")
    abk_sizew1 = fields.Float("Size W 1")
    abk_sizew2 = fields.Float("Size W 2")
    abk_stockamt = fields.Integer("Stockamt")
    abk_weight = fields.Float("Weight")
    abk_trimsize1 = fields.Float("Trim Size 1")
    abk_trimsize2 = fields.Float("Trim Size 2")
    abk_trimunit = fields.Char("Trim Unit")
    abk_remark = fields.Text("Remark")
    abk_chinese_name = fields.Char("Chinese Name")
    abk_jp = fields.Char("JP")
    abk_weight_unit = fields.Char("Weight Unit")
    abk_localcost = fields.Char("Local Cost")
    abk_unitpce = fields.Char("Unit pce")
    abk_localpce = fields.Char("Local pce")
    abk_pcecurre = fields.Char("pcecurr")
    abk_fixcost = fields.Boolean("Fix cost")
    abk_fixrate = fields.Boolean("Fix Rate")
    abk_color = fields.Char("Color")
    abk_papertype = fields.Char("Paper Type")
    abk_rate = fields.Char("Rate")
    abk_costcurr = fields.Char("costcurr")
    abk_qty = fields.Float("qty")
    abk_minqty = fields.Float("minqty")
    abk_poqty = fields.Float("poqty")
    abk_recqty = fields.Float("recqty")
    abk_holdqty = fields.Float("holdqty")
    abk_prodqty = fields.Float("prodqty")
    abk_matweight = fields.Float("matweight")
    abk_matunit = fields.Char("matunit")
    abk_workqty = fields.Float("workqty")
    abk_insize = fields.Char("insize")
    abk_paperquality = fields.Char("paperquality")
    abk_tranin = fields.Integer("tranin")


class ProductProductCustom(models.Model):
    _inherit = 'product.product'

    abk_hs_code = fields.Many2one("abk.hscommodity", string="HS Code")

class ABKProductClass(models.Model):
    _name = 'abk.product.class'
    _description = 'Product Class'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKWarranty(models.Model):
    _name = 'abk.warranty'
    _description = 'Warranty'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKHeadAsmAnalysis(models.Model):
    _name = 'abk.head.analysis'
    _description = 'Head/Asm Analysis'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKMaterialAnalysis(models.Model):
    _name = 'abk.material.analysis'
    _description = 'Material Analysis'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKReferenceCategory(models.Model):
    _name = 'abk.reference.category'
    _description = 'Reference Category'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKHSCommodity(models.Model):
    _name = 'abk.hscommodity'
    _description = 'HS Commodity'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)


class ABKFSCClaim(models.Model):
    _name = 'abk.fscclaim'
    _description = 'FSC Claim'
    _order = "sequence, name, id"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1)
