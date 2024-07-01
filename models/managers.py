from odoo import models,fields,api


class manager(models.Model):
    _name='manager'
    _description = 'menage all managers'

    name = fields.Char()
    id = fields.Integer()
    address = fields.Text()
    phone = fields.Char(copy=False)
    age = fields.Integer()
    salary = fields.Float()
    bonus = fields.Float()
    total_salary = fields.Float('total salary',compute='_compute_total_salary')
    employee_ids = fields.One2many(comodel_name='employee',inverse_name='manager_id')



    @api.depends('salary','bonus')
    def _compute_total_salary(self):
        for rec in self:
            rec.total_salary = rec.salary + rec.bonus


    _sql_constraints =[
        ('unique_phone','unique(phone)','this phone already exist')
    ]