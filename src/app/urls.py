from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name="welcome"),
    path('service', service, name="service"),
    path('service-sous/<int:id>/', under_service, name="sous-service"),
    path('confirmation', payment, name='payment'),
    path('postData', postData, name='postData')
]
