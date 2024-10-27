from rest_framework.routers import DefaultRouter
from .views import CatecoryViewSet, TransactionViewSet, BudgetViewSet

router = DefaultRouter()
router.register(r'categories', CatecoryViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'budgets', BudgetViewSet)

urlpatterns = router.urls