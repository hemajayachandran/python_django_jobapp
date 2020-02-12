from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyProfile
from .forms import CompanyProfileForm

# Create your views here.
def company_profile(request):
    context = {}
    context['form'] = CompanyProfileForm()
    return render(request, 'company_profile.html', context)

