
from django.urls import path, include 
from .api import SimpleApI
  
urlpatterns = [ 
    path('api/insert_data', SimpleApI.as_view() ), 
] 