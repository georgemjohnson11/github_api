from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from email_service import views

router = routers.DefaultRouter()
router.register(r'api', views.detail_via_API, 'api')
urlpatterns = [
    path('api/', include('email_service.urls')),
    path('submission/', views.contact),
    path('admin/', admin.site.urls),
]