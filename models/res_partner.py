from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange("vat")
    def _onchange_vat(self):
        if self.vat:
            self.vat = self.vat.upper()

    @api.model
    def create(self, vals):
        if vals.get("vat"):
            vals["vat"] = vals["vat"].upper()
        return super().create(vals)

    def write(self, vals):
        if vals.get("vat"):
            vals["vat"] = vals["vat"].upper()
        return super().write(vals)
