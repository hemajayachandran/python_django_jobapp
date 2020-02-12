from django.urls import path
from . import views

urlpatterns = [
        path('company_profile/', views.company_profile, name="company_profile"),
]