# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.product'

    warranty_time = fields.Integer(string='Warranty Time (Months)',
                                   help='Total number of months the warranty covers.')
