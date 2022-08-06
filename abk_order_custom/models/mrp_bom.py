from odoo import fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    mom = fields.Char(string='MoM')
