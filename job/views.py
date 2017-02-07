from django.shortcuts import render
from .models import JobPost

def job_list(request):
    jobs=JobPost.objects.all()
    return render(request,'jobs/job_list.html',{jobs:jobs})
