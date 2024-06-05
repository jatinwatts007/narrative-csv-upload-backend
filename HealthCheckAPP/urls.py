from django.urls import path
from HealthCheckAPP.views import HealthCheck

urlpatterns = [
    path('check/', HealthCheck.as_view()),
]