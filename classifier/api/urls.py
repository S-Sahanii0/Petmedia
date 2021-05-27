from django.urls import path
from classifier.api.views import (
    scan_image
)

urlpatterns = [
    path('scan', scan_image, name = "scan"),
]