from django.urls import path
from . import views
urlpatterns = [
    # path('order/create', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/update', views.OrderUpdate.as_view(), name='order_update'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/', views.OrdersOfUserListView.as_view(), name='my-orders'),

]
