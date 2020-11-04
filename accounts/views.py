from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import CreateView,UpdateView
from django.views.generic.base import TemplateView
from .forms import *
from .filters import *
from django.db.models import Count
from django.db.models import Q,F
# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"

class CustomerListView(generic.ListView):
    model = CustomerDetail
    context_object_name = 'customer'   # your own name for the list as a template variable
    template_name = 'accounts/customer_list.html'  # Specify your own template name/location
	
    def get_context_data(self,*args,**kwargs):
        context = super(CustomerListView,self).get_context_data(**kwargs)
        return context

    
    def get_queryset(self):
        queryset = self.request.GET.get('q')
        if queryset :
            object_list = CustomerDetail.objects.all().annotate(count=Count('ordersdetail')).filter(Q(mobile_number__icontains=queryset) | Q(name__icontains=queryset))
        else:
            object_list = CustomerDetail.objects.all().annotate(count=Count('ordersdetail'))
        return object_list
        
    # def total(self):
    #     t =  OrdersDetail.find_all_by_CustomerDetail(customer=OrdersDetail.customer_name)
    #     return t

# class OrderDetailView(generic.ListView):
#     model = OrdersDetail 
#     context_object_name = 'orderdata'
#     template_name = 'accounts/order_detail.html'
#     # queryset = OrdersDetail.objects.all()

#     # def get_object(self):
#     #     id_ = self.kwargs.get('id')
#     #     return get_object_or_404(OrdersDetail,id=id_)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['order_detail'] = OrdersDetail.objects.all()
#         return context
    
    
    # def get_queryset(self):
    #     queryset = OrdersDetail.objects.all().filter(Q(get_object(self)))
    #     return queryset
    
    # def total(self):
    #     order = OrdersDetail.objects.all().annotate(a = F('amount')-F('downPayment'))
    #     return order

class OrderListView(generic.ListView):
    model = OrdersDetail
    context_object_name = 'order_list'   # your own name for the list as a template variable
    queryset = OrdersDetail.objects.all()
    template_name = 'accounts/order_list.html'  # Specify your own template name/location

    def get_context_data(self,*args, **kwargs):
        context = super(OrderListView,self).get_context_data(**kwargs)
        context['order_list']=OrdersFilter(self.request.GET,queryset=OrdersDetail.objects.all())
        return context

class CustomerCreateView(CreateView):
	model = CustomerDetail
	fields = {'name','mobile_number','aadhar_card','address'}
	success_url = "/customers"

	def form_valid(self,form):
		return super().form_valid(form)



class OrderCreateView(CreateView):
    form_class = OrderForm
    model = OrdersDetail
    success_url = "/orders"
	
    def form_valid(self,form):
        return super(OrderCreateView,self).form_valid(form)

class OrderUpdateView(UpdateView):
    form_class = OrderForm
    model = OrdersDetail
    success_url = "/orders"
    template_name = 'accounts/ordersdetail_form.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(OrdersDetail,id=id_)
	
    # def form_valid(self,form):
    #     return super(OrderCreateView,self).form_valid(form)

