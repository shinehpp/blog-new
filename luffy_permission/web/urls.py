from django.conf.urls import url
from web.views import customer
from web.views import payment

urlpatterns = [

    url(r'^customer/list/$', customer.customer_list, name='customer-list'),
    url(r'^customer/add/$', customer.customer_add, name='customer-add'),
    url(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit, name='customer-edit'),
    url(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del, name='customer-del'),
    url(r'^customer/import/$', customer.customer_import, name='customer-import'),
    url(r'^customer/tpl/$', customer.customer_tpl, name='customer-tpl'),

    url(r'^payment/list/$', payment.payment_list, name='payment-list'),
    url(r'^payment/add/$', payment.payment_add, name='payment-add'),
    url(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit, name='payment-edit'),
    url(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del, name='payment-del'),

]
