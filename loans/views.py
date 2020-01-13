from django.shortcuts import render
from rest_framework import generics, status, viewsets 
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError

from .models import Loan
from.serializers import LoanSerializer

# Create your views here.

class LoanApplicationAPIView(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)

    def perform_destroy(self, instance):
        Loan_instance=self.get_object()
        user=self.request.user
        user=Loan_instance.user

        if user !=user:
            raise ValidationError("Sorry you are not authorized to delete this loan application!")
        Loan_instance.delete()

