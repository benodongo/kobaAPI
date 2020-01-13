from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LoanApplicationAPIView



urlpatterns = [
     #gets all user profiles and create a new profile
    path("new-loan",LoanApplicationAPIView.as_view(),name="new-loan"),
]