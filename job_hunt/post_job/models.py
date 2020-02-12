from django.db import models

# Create your models here.
class PostJobModel(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    JOB_TYPE = [
        ('WEBDEVELOPMENT', 'Web Development'),
        ('WEBDESIGNING', 'Web Designing'),
        ('ARTCULTURE', 'Art & Culture'),
        ('READWRITE', 'Read & Writing'),
    ]
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    OFFERED_SALARY = [
        ('0-3LAKHS', '0 to 3 Lakhs'),
        ('3-6LAKHS', '3 to 6 Lakhs'),
        ('6-12LAKHS', '6 to 12 Lakhs'),
    ]
    offered_salary = models.CharField(max_length=20, choices=OFFERED_SALARY)

    EXPERIENCE_REQUIRED = [
        ('0-3YEARS', '0 to 3 Years'),
        ('3-6YEARS', '3 to 6 Years'),
        ('6-12YEARS', '6 to 12 Years'),
    ]
    experience_required = models.CharField(max_length=20, choices=EXPERIENCE_REQUIRED)


    def __str__(self):
        return str(self.job_title)
