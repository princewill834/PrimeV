from django.urls import path
from .views import index,coupon,customer,postDetail, shareItem,withdraw

urlpatterns = [
   path('',index, name='index'),
   path('coupon/',coupon, name='coupon'),
   path('customer/',customer, name='customer_dashboard'),
   path('post-detail/<slug:slug>/', postDetail, name='post_detail'),
   path('share-item/<slug:slug>', shareItem, name='share_item'),
   path('withdraw/', withdraw, name='withdraw')
]