from django.urls import path
from . import views
urlpatterns = [
    path('', views.HRView.as_view(), name='human_resource'),
    path('createorder/',views.CreateWeekOrderView.as_view(),name='hr_create_order'),
    path('reports/', views.report_view, name='hr_reports'),
    path('reports/pdf', views.OrderPdfView.as_view(), name='report_now'),
    path('reports/todaysorder',views.TodayOrderView.as_view(), name='todaysorder'),
    path('reports/orderbyfood', views.OrderByFoodView.as_view(), name='orderbyfood'),
    path('reports/foodsummary', views.FoodSummaryView.as_view(), name='foodsummary'),
    path('update/<int:pk>/',views.UpdateWeekOrderView.as_view(),name='updateweekorder')
]