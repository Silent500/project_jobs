from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    verification_code = models.CharField(max_length=6, null=True, blank=True)

    class Meta:
        db_table = "app_users"

class job(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    specification = models.TextField(max_length=500)
    salery_range = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    class Meta:
	    db_table = "app_jobs"
            
# https://byjus.com/gate/anomalies-in-dbms-notes/