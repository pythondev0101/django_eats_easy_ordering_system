from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('social_django.urls', namespace="social")),
    path('comments/<int:pk>/',views.CommentView.as_view(),name='comment')
]
