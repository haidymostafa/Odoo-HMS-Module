from odoo import models, fields
from odoo import api
from odoo.exceptions import ValidationError, UserError


class HospitalCustomer(models.Model):
    _inherit = "res.partner"
    related_patient_id = fields.Many2one(comodel_name="hms.patient")

    # Validation For Customer email isn't Equal Patient Email
    @api.constrains("email")
    def validate_customer_patient_email(self):
        print(print(self.env['hms.patient'].search([("patient_email", "=", self.email)], limit=1)))
        if len(self.env['hms.patient'].search([("patient_email", "=", self.email)], limit=1)) != 0:
            raise ValidationError('Sorry This Email Already Exist')

    # Prevent User User to Delete Customer linked to An Patient
    @api.multi
    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise UserError(f"Sorry You Can't Delete This Customer Because it's Linked to Patient")

        super().unlink()