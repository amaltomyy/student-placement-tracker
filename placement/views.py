
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    Job,
    StudentProfile,
    Application,
    StudentJobTracker,
)

from .forms import (
    StudentRegistrationForm,
    StudentProfileForm,
    StudentJobTrackerForm,
)


def home(request):
    return render(request, 'placement/home.html')


def job_list(request):
    jobs = Job.objects.all()
    return render(
        request,
        'placement/job_list.html',
        {'jobs': jobs}
    )


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                'Account created successfully!'
            )
            return redirect('student_tracker')
    else:
        form = StudentRegistrationForm()

    return render(
        request,
        'placement/register.html',
        {'form': form}
    )


@login_required
def profile(request):
    student_profile, created = StudentProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'phone': '',
            'course': '',
            'skills': '',
        }
    )

    if request.method == 'POST':
        form = StudentProfileForm(
            request.POST,
            instance=student_profile
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Profile saved successfully!'
            )
            return redirect('profile')
    else:
        form = StudentProfileForm(instance=student_profile)

    return render(
        request,
        'placement/profile.html',
        {'form': form}
    )


@login_required
def apply_job(request, job_id):
    if request.method == 'POST':
        student_profile, created = StudentProfile.objects.get_or_create(
            user=request.user,
            defaults={
                'phone': '',
                'course': '',
                'skills': '',
            }
        )

        job = get_object_or_404(Job, id=job_id)

        application, created = Application.objects.get_or_create(
            student=student_profile,
            job=job
        )

        if created:
            messages.success(
                request,
                'Application submitted successfully!'
            )
        else:
            messages.info(
                request,
                'You have already applied for this job.'
            )

    return redirect('job_list')


@login_required
def my_applications(request):
    student_profile, created = StudentProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'phone': '',
            'course': '',
            'skills': '',
        }
    )

    applications = Application.objects.filter(
        student=student_profile
    ).select_related('job').order_by('-applied_at')

    return render(
        request,
        'placement/my_applications.html',
        {'applications': applications}
    )


@login_required
def student_tracker(request):
    if request.method == 'POST':
        form = StudentJobTrackerForm(request.POST)

        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.student = request.user
            tracker.save()

            messages.success(
                request,
                'Job or internship saved successfully!'
            )
            return redirect('student_tracker')
    else:
        form = StudentJobTrackerForm()

    opportunities = StudentJobTracker.objects.filter(
        student=request.user
    ).order_by('-applied_date')

    return render(
        request,
        'placement/student_tracker.html',
        {
            'form': form,
            'opportunities': opportunities,
        }
    )


@login_required
def edit_tracked_opportunity(request, opportunity_id):
    opportunity = get_object_or_404(
        StudentJobTracker,
        id=opportunity_id,
        student=request.user
    )

    if request.method == 'POST':
        form = StudentJobTrackerForm(
            request.POST,
            instance=opportunity
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Application updated successfully!'
            )
            return redirect('student_tracker')
    else:
        form = StudentJobTrackerForm(instance=opportunity)

    return render(
        request,
        'placement/edit_tracked_opportunity.html',
        {
            'form': form,
            'opportunity': opportunity,
        }
    )