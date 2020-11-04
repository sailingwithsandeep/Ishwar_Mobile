from django.urls import path,include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    path('add/',views.OrderCreateView.as_view(),name='add_order'),
    path('orders/',views.OrderListView.as_view(),name='orders'),
    path('addcustomer/',views.CustomerCreateView.as_view(),name='add_customer'),
    path('add/<int:id>',views.OrderUpdateView.as_view(),name='order_edit'),
    path('customers/',views.CustomerListView.as_view(),name='customers'),
    # path('customers/orderdetails/',views.OrderDetailView.as_view(),name='order_detail')
]