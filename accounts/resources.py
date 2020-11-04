from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *


class orderResource(resources.ModelResource):
    customer_name = fields.Field(
        column_name='name',
        attribute='customer_name',
        widget=ForeignKeyWidget(CustomerDetail,'name')
    )
    # number = fields.Field(
    #     column_name='number',
    #     attribute='number',
    #     widget=ForeignKeyWidget(CustomerDetail,'number')
    # )
    class Meta:
        model = OrdersDetail
        import_id_fields = ('customer_name','mobile_Model','amount','downPayment','purchase_Date','installments','emi_Date','pending_installments','status')
        export_order = ('customer_name','mobile_Model','amount','downPayment','purchase_Date','installments','emi_Date','pending_installments','status')
        exclude = ('id',)
        skip_unchanged = True
        fields = ['customer_name','mobile_Model','amount','downPayment','purchase_Date','installments','emi_Date','pending_installments','status']