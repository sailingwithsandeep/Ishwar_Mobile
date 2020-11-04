from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
#from .resources import *
# Register your models here.
from .resources import *
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


@admin.register(CustomerDetail)
class listadmin(admin.ModelAdmin):
  fields = ['name','mobile_number','address','aadhar_card']
  list_display = ['name','mobile_number']
  search_fields = ['name',' mobile_number']

class orderadmin(ImportExportModelAdmin):
    resource_class = orderResource
    search_fields = ('cutomer_name','mobile_Model',)
    list_display= ('customer_name','mobile_Model','amount','downPayment','purchase_Date','installments','emi_amount','emi_Date','pending_installments','status','total','pending_amount',)
    list_filter = (('purchase_Date', DateRangeFilter),('emi_Date',DateRangeFilter),'status')



admin.site.register(OrdersDetail,orderadmin)