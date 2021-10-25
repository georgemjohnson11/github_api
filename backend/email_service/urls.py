from django.urls import path
from . import views

urlpatterns = [
    path('', views.detail_via_package, name='detail_via_package'),
    path('<slug:repo>/', views.detail_via_API, name='detail_via_API'),
]