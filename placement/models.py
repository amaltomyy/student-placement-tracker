
from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    skills = models.TextField(blank=True)
    deadline = models.DateField()

    def __str__(self):
        return self.title + " - " + self.company


class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    def __str__(self):
        return self.student.user.username + " - " + self.job.title


class StudentJobTracker(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    opportunity_type = models.CharField(
        max_length=20,
        choices=[
            ('Job', 'Job'),
            ('Internship', 'Internship'),
        ],
        default='Job'
    )
    applied_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )
    interview_date = models.DateField(
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.company} - {self.job_title}"