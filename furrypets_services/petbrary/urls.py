from django.urls import path
from .views import PetsAPIView, CareAndHealthAPIView

urlpatterns = [
    path('pets-category', PetsAPIView.as_view(), name='watching-pets'),
    path('care-and-health-category', CareAndHealthAPIView.as_view(), name='watching-care-and-health')
]
