from django import forms

from .models import PostJobModel

class PostJobForm(forms.ModelForm):

    class Meta:
        model = PostJobModel
        fields = ('job_title', 'job_description', 'job_type', 'offered_salary', 'experience_required',)
        labels = {'job_title': 'Job Title', 'job_description': 'Description', 'job_type': 'Job Type', 'offered_salary': 'Offered Salary', 'experience_required': 'Experience Required'}