from django.shortcuts import render

from rest_framework import viewsets
from .models import Transaction, Budget, Category
from .serializers import TransactionSerializer, BudgetSerializer, CategorySerializer

class CatecoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the transactio owner
        serializer.save(user=self.request.user)    

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        # Automatically assign the logged-in uder asthe budget owner
        serializer.save(user=self.request.user)
