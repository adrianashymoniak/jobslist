from django.shortcuts import render

from jobs.models import Job


def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})
