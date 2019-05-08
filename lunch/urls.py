from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('order/create/', views.CreateOrderView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='myorder-detail'),
    path('orders/', views.OrdersOfUserListView.as_view(), name='my-orders'),

]
