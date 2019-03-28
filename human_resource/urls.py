from django.urls import path
from . import views
urlpatterns = [
    path('', views.HRView.as_view(), name='human_resource'),
    path('products/', views.hr_products, name='hr_products'),
]