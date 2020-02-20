from django.urls import path
from .views import CompanyProfileView

urlpatterns = [
        path('company_profile/', CompanyProfileView.as_view(), name="company_profile"),
        path('company_profile/(?P<pk>\d+)/', CompanyProfileView.as_view(), name="company_profile"),
        
]