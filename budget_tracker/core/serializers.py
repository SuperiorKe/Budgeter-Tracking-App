from rest_framework import serializers
from .models import Transaction, Budget, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested Category details

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'category', 'amount', 'Transaction_type', 'date', 'description']


class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta: 
        model = Budget
        fields = ['id', 'user', 'category', 'limit', 'period']
        