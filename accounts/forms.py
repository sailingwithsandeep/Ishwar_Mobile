from django import forms
from .models import *
from django.core import serializers
from bootstrap_datepicker_plus import DatePickerInput

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = {'name','mobile_number','aadhar_card','address'}
        lables = {'name':'Name','mobile_number':'Mobile Number','aadhar_card':'Aadhar Proof','address':'Address'}

        def __init__(self,*args,**kwargs):
            super(CustomerForm,self).__init__(*args, **kwargs)

class OrderForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
            super(OrderForm,self).__init__(*args, **kwargs)
            
    field_order = ['customer_name','mobile_Model','amount','downPayment','purchase_Date','installments','emi_amount','total','pending_amount','status','pending_installments','emi_Date','remarks',]



    class Meta:
        model = OrdersDetail
        fields = {'customer_name','mobile_Model','amount','downPayment','purchase_Date','installments','pending_installments','emi_Date','emi_amount','total','pending_amount','status','remarks'}
        widgets = {
            'purchase_Date': DatePickerInput(options={
                    "showClear": True,
                    "showTodayButton": True,
                }), # default date-format %m/%d/%Y will be used
            'emi_Date': DatePickerInput(options={
                    "showClear": True,
                    "showTodayButton": True,
                }),
            'pay_date':DatePickerInput(options={
                'showClear':True,
                'showTodayButton':True,
            })
        }
        lables = {'customer_name':'Customer Name','mobile_Model':'Mobile Model','amount':'Amount','downPayment':'DownPayment','purchase_date':'Purchase Date','installments':'Installments Option','pending_installments':'Pending Installments','emi_Date':'EMI Date','emi_amount':'EMI Amount','total':'Total','status':'Status','pending_amount':'Pending Amount','remarks':'Remarks'}
       
       
        