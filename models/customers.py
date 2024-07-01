from odoo import models,fields,api
from odoo.exceptions import ValidationError


class customer(models.Model):
    _name='customer'
    _description = 'menage all customers'
    _inherit = ['mail.thread','mail.activity.mixin']

    name=fields.Char()
    address = fields.Text()
    phone = fields.Char(tracking=1,copy=False)
    order_date = fields.Date()
    active = fields.Boolean(default=True)
    total = fields.Integer(compute='_compute_total')
    product_ids = fields.Many2many(comodel_name='product')
    delivery_date=fields.Date()
    state=fields.Selection([
        ('new','New'),
        ('in_progress','In Progress'),
        ('done','Done'),
    ],default='new',tracking=1)


    _sql_constraints =[
        ('unique_phone','unique(phone)','this phone already exist')
    ]


    @api.depends('product_ids')
    def _compute_total(self):
        for rec in self:
            t = 0
            for line in rec.product_ids:
                t += line.price
            rec.total = t


    @api.constrains('delivery_date','order_date')
    def check_date(self):
        for rec in self:
            if rec.delivery_date < rec.order_date:
                raise ValidationError('invalid order date or delivery date')




