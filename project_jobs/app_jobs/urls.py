
from django.urls import path
from . import views
urlpatterns = [
    path('jobs/', views.job_index, name="job.index"),
    path('job/show/', views.job_show, name="job.show"),
]
