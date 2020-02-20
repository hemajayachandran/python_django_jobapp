from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import CompanyProfile
from .forms import CompanyProfileForm
from django.views.generic import TemplateView

# Create your views here.
class CompanyProfileView(TemplateView):
    template_name = 'company_profile.html'

    def get(self, request):
        form = CompanyProfileForm()
        companys = CompanyProfile.objects.all()
        print(companys)
        args = {'form': form, 'companys': companys}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CompanyProfileForm(request.POST)
        company = CompanyProfile()
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            since = form.cleaned_data['since']
            company_description = form.cleaned_data['company_description']
            team_size = form.cleaned_data['team_size']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            company = CompanyProfile(company_name=company_name, 
                                     since=since,
                                     company_description=company_description,
                                     team_size=team_size,
                                     phone_number=phone_number,
                                     email=email,
                                     website=website)
            company.save()
            
        args = {'form': form, 'company': company}
        return render(request, self.template_name, args)
