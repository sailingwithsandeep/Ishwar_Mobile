from django.db import models
from datetime  import datetime,date
from django.urls import reverse
from django.db.models import Count
from django.db.models import Q,F
from django.conf.global_settings import DATETIME_INPUT_FORMATS, DATE_INPUT_FORMATS
statuslist = [('Pending','Pending'),('Done','Done')]

# Create your models here.
class CustomerDetail(models.Model):
    name = models.CharField(max_length=256,unique=True)
    mobile_number = models.BigIntegerField(unique=True)
    aadhar_card = models.ImageField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class OrdersDetail(models.Model):
    customer_name = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE,to_field='name',)
    #cutomer_number = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE,to_field='mobile_number')
    mobile_Model = models.CharField(max_length=256)
    amount = models.FloatField()
    downPayment = models.FloatField()
    purchase_Date = models.DateField()
    installments = models.FloatField()
    emi_Date = models.DateField()
    emi_amount = models.FloatField(default=0)
    status = models.CharField(max_length=256,choices=statuslist)
    pending_installments = models.FloatField(default=0)
    total = models.FloatField(default=0)
    pending_amount = models.FloatField(default=0)
    remarks = models.TextField(blank=True,default='Collection:\n1st:\n2nd:\n3th:\n4th:\n5th:\n6th:\n7th:\n8th:\n9th:\n10th:\n11th:\n12th:',max_length=256)
    # mobile = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE,to_field='mobile_number',related_name='number',blank=True,null=True)
    #due_Amount = models.DecimalField(get_due_amount(amount,downPayment),max_digits=10,decimal_places=2)
    

    def __str__(self):
        return str(self.customer_name)    

    def get_absolute_url(self):
        return reverse("accounts:order_edit", kwargs={"id": self.id})

    def get_absolute_url(self):
        return reverse("accounts:order_detail",kwargs={"id":self.id})
    
    
    # def emi_amount(self):
    #     p = self.amount - self.downPayment
    #     # r = self.interest
    #     t = self.installments 
    #     # r = r / (12 * 100) # one month interest 
    #     # #t = t * 12 # one month period 
    #     # emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1) 
    #     emi = p/t
    #     return round(emi,2)
            

    # def total(self):
    #     return sum([CustomerDetail.objects.all().annotate(count=Count('ordersdetail')) for customer in self.emi_amount.all() ])

    # def pending_amount(self):
    #     emi_amount()
    #     p = self.amount - self.downPayment
    #     return p


    class Meta:
        ordering = ["emi_Date"]


    