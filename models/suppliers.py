from odoo import models,fields


class supplier(models.Model):
    _name='supplier'
    _description = 'menage all suppliers'

    name = fields.Char()
    id = fields.Integer()
    address = fields.Text()
    phone = fields.Char(copy=False)
    product_ids = fields.Many2many(comodel_name="product")


    _sql_constraints =[
        ('unique_phone','unique(phone)','this phone already exist')
    ]