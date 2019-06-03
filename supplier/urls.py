from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.SupplierView.as_view(), name='supplier_create'),
    path('',views.SupplierDetailView.as_view(),name='supplier'),
    path('update/<int:pk>',views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('createproduct/',views.CreateProductView.as_view(),name='addproduct'),
    path('updateproduct/<int:pk>',views.UpdateProductView.as_view(),name='editproduct'),
]