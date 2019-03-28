from django.urls import path
from . import views
urlpatterns = [
    path('', views.HRView.as_view(), name='human_resource'),
    path('createorder/',views.CreateWeekOrderView.as_view(),name='hr_create_order')
]