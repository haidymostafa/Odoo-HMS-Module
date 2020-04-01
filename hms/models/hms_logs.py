from odoo import models,fields
from datetime import datetime, timedelta


class HospitalLogs(models.Model):
    _name = "hms.logs"
    created_by = fields.Many2one('res.users','Created By', default=lambda self: self.env.user)
    date = fields.Datetime(string="Date",default=fields.datetime.now())
    description = fields.Text(string="Description")
