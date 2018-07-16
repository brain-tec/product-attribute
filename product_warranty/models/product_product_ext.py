from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    warranty_time = fields.Integer(string='Warranty Time (Months)',
                                   help='Total number of months the warranty covers.')
