from django.db import models

# Create your models here.
class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=200, primary_key=True, unique=True)
    since = models.IntegerField(help_text="Year")
    company_description = models.TextField()
    team_size = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, help_text="Enter with area code")
    email = models.EmailField(unique=True)
    website = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return str(self.company_name)

