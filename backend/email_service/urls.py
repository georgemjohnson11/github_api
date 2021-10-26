from django.urls import path, re_path
from . import views
app_name = 'github'
urlpatterns = [
    path(r'<slug:owner>/<slug:repo>/', views.detail_via_API, name='detail_via_API'),
    path('react/', views.detail_via_React, name='detail_via_React'),
    path('github/', views.detail_via_package, name='detail_via_package'),
    path('contact/', views.contact, name='contact'),
    re_path(r'', views.detail_via_API, name='home'),
]