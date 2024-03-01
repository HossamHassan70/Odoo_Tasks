from odoo import fields, models


class Form(models.Model):
    _name = 'form'
    _description = 'Todo Form'

    name = fields.Char(required=True)
    number = fields.Char(required=True)
    tag = fields.Char()
    state = fields.Selection([
        ('add', 'Add'),
        ('doing', 'Doing'),
        ('done', 'Done')],
        string='State', default='new')
    file = fields.Binary()
    assign_to = fields.Many2one('res.users')
    description = fields.Text()
