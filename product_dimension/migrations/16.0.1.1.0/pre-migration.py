##############################################################################
# Copyright (c) 2023 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

# Script copied and adapted from v12.

from openupgradelib import openupgrade

field_renames = [
    ("product.template", "product_template", "length", "product_length"),
    ("product.template", "product_template", "height", "product_height"),
    ("product.template", "product_template", "width", "product_width"),
    ("product.product", "product_product", "length", "product_length"),
    ("product.product", "product_product", "height", "product_height"),
    ("product.product", "product_product", "width", "product_width"),
]


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    openupgrade.rename_fields(env, field_renames)
