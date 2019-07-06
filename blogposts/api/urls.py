from django.urls import path, include

from api import views

urlpatterns = [
    path('posts/', views.external_api_view, name='external-api-view'),    
]