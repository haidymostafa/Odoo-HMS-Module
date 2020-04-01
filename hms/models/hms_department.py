from odoo import models,fields

class HospitalDepartment(models.Model):
    _name = "hms.department"
    name = fields.Char("Department Name")
    Capacity = fields.Integer("Capacity")
    is_opened = fields.Boolean("Is Opened")
    patient_id = fields.One2many(comodel_name="hms.patient",inverse_name="dept_id")