from odoo import models,fields,api


class employee(models.Model):
    _name='employee'
    _description = 'menage all employees'

    name = fields.Char()
    id = fields.Integer()
    address = fields.Text()
    phone = fields.Char(copy=False)
    age = fields.Integer()
    salary = fields.Float()
    bonus = fields.Float()
    total_salary = fields.Float('total salary',compute='_compute_total_salary',readonly=False)
    manager_id = fields.Many2one(comodel_name='manager')



    @api.depends('salary','bonus')
    def _compute_total_salary(self):
        for rec in self:
            rec.total_salary = rec.salary + rec.bonus



    _sql_constraints =[
        ('unique_phone','unique(phone)','this phone already exist')
    ]

