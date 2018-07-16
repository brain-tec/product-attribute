from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warranty_time = fields.Integer(string='Warranty Time (Months)',
                                   compute='_compute_default_warranty_time',
                                   inverse='_set_default_warranty_time',
                                   help='Total number of months the warranty covers.')

    @api.one
    def _set_warranty_time(self):
        if len(self.product_variant_ids) == 1:
            self.product_variant_ids.warranty_time = self.warranty_time

    @api.depends('product_variant_ids', 'product_variant_ids.warranty_time')
    def _compute_warranty_time(self):
        unique_variants = self.filtered(
            lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.warranty_time = template.product_variant_ids.warranty_time
        for template in (self - unique_variants):
            template.warranty_time = False