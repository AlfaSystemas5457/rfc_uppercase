from odoo import api, SUPERUSER_ID


def post_init_upper_vat(env):
    partners = env["res.partner"].search([("vat", "!=", False)])

    for partner in partners:
        partner.vat = partner.vat.upper()
