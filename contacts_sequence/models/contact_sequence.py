# -*- coding: utf-8 -*-

from odoo import fields, models, _,api


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    reference = fields.Char(string='Contact Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))

    @api.model
    def create(self,vals):
        print("hjhj")
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('res.partner') or _('New')
            res = super(ResPartner, self).create(vals)
            print("res", res)
            return res

    def update_contacts(self):
        records = self.env['res.partner'].search([])
        for record in records:
        # if record.reference == 'New':
            # sequence_no = 1
            record.write({
                'reference': self.env['ir.sequence'].next_by_code('res.partner')
            })
 # if not order_line.number:
 #                serial_no = 1
 #                for line in order_line.mapped('order_id').order_line:
 #                    line.number = serial_no
 #                    serial_no += 1

  # sequence_id = self.env['ir.sequence'].search([('code', '=', 'your.sequence.code')])
  #           sequence_pool = self.env['ir.sequence']
  #           application_no = sequence_pool.sudo().get_id(sequence_id.id)
  #           self.write({'application_no': application_no})
#
