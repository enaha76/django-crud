# app_21007/resources.py
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Product, ProductFamily

class ProductResource(resources.ModelResource):
    productfamily = fields.Field(
        column_name='productfamily label',
        attribute='productfamily',
        widget=ForeignKeyWidget(ProductFamily, 'label'))

    class Meta:
        model = Product
        import_id_fields = ['label', 'price_unit', 'code', 'productfamily']
        fields = ('label', 'price_unit', 'code', 'productfamily')
