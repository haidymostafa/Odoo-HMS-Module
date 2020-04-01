from odoo import models,fields

class HospitalDoctor(models.Model):
    _name = "hms.doctor"
    _rec_name = "fname"
    fname = fields.Char("First Name")
    lname = fields.Char("Last Name")
    doc_img = fields.Binary("Doctor Image")