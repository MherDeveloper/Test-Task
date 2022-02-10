from django.urls import path
from .views import VisitViewSet

urlpatterns = [
    path('visit/', VisitViewSet.as_view({'post': 'create', 'get': 'list'}), name="visit")
]