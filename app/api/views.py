from django.shortcuts import render
from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer