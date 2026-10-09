
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import StudentProfile, StudentJobTracker


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['phone', 'course', 'skills']


class StudentJobTrackerForm(forms.ModelForm):
    class Meta:
        model = StudentJobTracker
        fields = [
            'company',
            'job_title',
            'opportunity_type',
            'applied_date',
            'status',
            'interview_date',
            'notes',
        ]

        widgets = {
            'applied_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'interview_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }