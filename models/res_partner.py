from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange("vat")
    def _onchange_vat(self):
        if self.vat:
            self.vat = self.vat.upper()

    @api.model
    def create(self, vals_list):
        if isinstance(vals_list, dict):
            vals_list = [vals_list]

        for vals in vals_list:
            if vals.get("vat"):
                vals["vat"] = vals["vat"].upper()

        return super().create(vals_list)

    def write(self, vals):
        if vals.get("vat"):
            vals["vat"] = vals["vat"].upper()
        return super().write(vals)
