from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import ApiTaskViewSet

router = SimpleRouter()
router.register(r'1.0/task', ApiTaskViewSet)
