from django.shortcuts import render, redirect, get_object_or_404

from .forms import JobForm
from .models import Job


def home(request):
    jobs = Job.objects.all()
    languages = set((map(lambda x: x.language, jobs)))
    context = {
        'jobs': jobs,
        'languages': languages,
    }
    return render(request, 'home.html', context)


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('details', pk=job.pk)
        else:
            context = {'form': form}
            return render(request, 'create-new-job.html', context)
    else:
        form = JobForm()
        context = {'form': form}
        return render(request, 'create-new-job.html', context)


def details(request, pk):
    job = get_object_or_404(Job, pk=pk)
    context = {'job': job}
    return render(request, 'details.html', context)
