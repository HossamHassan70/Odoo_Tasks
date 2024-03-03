from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hms.patient'
    _description = "Hospital Management System"
    _rec_name = "full_name"

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    ])
    pcr = fields.Boolean()
    image = fields.Binary(attachment=True, store=True)
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    full_name = fields.Char(compute='_compute_full_name', store=True)
    department_id = fields.Many2one('hms.department')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            if record.last_name:
                record.full_name = f"{record.first_name} {record.last_name}"
            else:
                record.full_name = record.first_name

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - (
                            (today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            else:
                record.age = 0
