from django.urls import path
from . import views
urlpatterns = [
    path('', views.HRView.as_view(), name='human_resource'),
]