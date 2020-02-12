from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostJobForm

# Create your views here.
def post_job(request):
    context = {}
    context['form'] = PostJobForm()
    return render(request, 'post_job.html', context)
