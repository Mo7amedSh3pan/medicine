from odoo import models,fields,api


class product(models.Model):
    _name='product'
    _description = 'menage all products'


    name = fields.Char()
    id = fields.Integer()
    price=fields.Float()
    supplier_ids = fields.Many2many(comodel_name='supplier')