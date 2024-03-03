from odoo import fields, models


class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo Form'

    name = fields.Char(required=True)
    number = fields.Char(required=True)
    tag = fields.Char()
    state = fields.Selection([
        ('add', 'Add'),
        ('doing', 'Doing'),
        ('done', 'Done')],
         default='add')
    file = fields.Binary()
    description = fields.Text()
