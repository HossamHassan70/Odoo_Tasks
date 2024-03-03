from odoo import models, fields


class Department(models.Model):
    _name = 'hms.department'
    _description = "Hospital Departments"

    name = fields.Char(required=True)
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients = fields.One2many('hms.patient', 'department_id')
