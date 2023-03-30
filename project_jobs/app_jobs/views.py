from django.shortcuts import render

# Create your views here.
def job_index(request):
    return render(request, 'jobs/index.html')

def job_show(request):
    return render(request, 'jobs/show.html')