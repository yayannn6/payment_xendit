from odoo import _, api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    currency_field = fields.Float("Currency Field")