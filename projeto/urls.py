from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

urlpatterns = [
    path('', include('projeto.core.urls')),
    path('produto/', include('projeto.produto.urls')),
    
]
