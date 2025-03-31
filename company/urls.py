from rest_framework.routers import DefaultRouter
from django.urls import path, include

from company.views import CompanyViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename="company")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "company"
