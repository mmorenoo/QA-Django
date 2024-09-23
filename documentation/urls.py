from django.urls import path 
from . import views    

urlpatterns = [
    path('', views.hello ),
    path('documentation/', views.documentation)
]