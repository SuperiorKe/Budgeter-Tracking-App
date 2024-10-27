from django.db import models
from django.contrib.auth.models import User

# category to categorize spending
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
     
# Transaction (to track expenses and income)
class Transaction(models.Model):
    CATEGORY_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    Transaction_type = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    date = models.DateTimeField(auto_now_add=True, null=True)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"



# Budget (to set monthly or category budgets)
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    period = models.CharField(max_length=50) #e.g, "Monthly", "Weekly"

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.limit}"