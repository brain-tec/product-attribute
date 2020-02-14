import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-product-attribute",
    description="Meta package for oca-product-attribute Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-product_assortment',
        'odoo13-addon-product_code_unique',
        'odoo13-addon-product_cost_security',
        'odoo13-addon-product_manufacturer',
        'odoo13-addon-product_packaging_dimension',
        'odoo13-addon-product_restricted_type',
        'odoo13-addon-product_secondary_unit',
        'odoo13-addon-product_sequence',
        'odoo13-addon-product_supplierinfo_for_customer',
        'odoo13-addon-product_template_tags',
        'odoo13-addon-stock_production_lot_firmware_version',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
