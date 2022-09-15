from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name="welcome"),
    path('service', service, name="service"),
    path('service-sous', under_service, name="sous-service")
]
