from django import forms
from .models import CompanyProfile

class CompanyProfileForm(forms.ModelForm):
    company_name = forms.CharField(max_length=200, required=True, label = "Company Name")
    since = forms.IntegerField(help_text="Year")
    company_description = forms.CharField(label="Description")
    team_size = forms.CharField(max_length=200, label="Team Size")
    phone_number = forms.CharField(max_length=20, help_text="Enter with area code", label="Phone Number")
    email = forms.EmailField(required=True, label="Email")
    website = forms.CharField(label="Website")

    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'since', 'company_description', 'team_size', 'phone_number', 'email', 'website',)