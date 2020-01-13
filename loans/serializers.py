from rest_framework import serializers
from .models import Loan

#serialize the loan model
class LoanSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Loan
        fields = '__all__'
