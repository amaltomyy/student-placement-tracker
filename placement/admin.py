
from django.contrib import admin
from .models import StudentProfile, Job, Application, StudentJobTracker


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'course')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'deadline')
    search_fields = ('title', 'company', 'location')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'job', 'applied_at', 'status')
    list_filter = ('status', 'applied_at')
    search_fields = ('student__user__username', 'job__title', 'job__company')


@admin.register(StudentJobTracker)
class StudentJobTrackerAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'company',
        'job_title',
        'opportunity_type',
        'status',
        'applied_date',
    )
    list_filter = ('status', 'opportunity_type')
    search_fields = ('student__username', 'company', 'job_title')