"""eats_easy_ordering_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import routers
from django.conf.urls import url
from django.conf import settings
from core.views import UserViewSet,ProductViewSet,HRViewSet,OrderViewSet
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from lunch.views import get_product_detail
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products',ProductViewSet)
router.register(r'hr',HRViewSet)
router.register(r'orders',OrderViewSet)
urlpatterns = [
    path('', RedirectView.as_view(url='/lunch/order/create', permanent=True)),
    path('admin/', admin.site.urls),
    path('web/', include('core.urls')),
    path('lunch/', include('lunch.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('hr/', include('human_resource.urls')),
    path('supplier/',include('supplier.urls')),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path('ajax/getproduct/', get_product_detail, name='get_product_detail'),
]

# For debug-toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


from django.conf.urls.static import static




# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
