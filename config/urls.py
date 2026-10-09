
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from placement import views

urlpatterns = [
    # Student pages
    path('', views.home, name='home'),
    path('jobs/', views.job_list, name='job_list'),

    # Student registration and login
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='placement/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Student profile and applications
    path('profile/', views.profile, name='profile'),
    path(
        'apply/<int:job_id>/',
        views.apply_job,
        name='apply_job'
    ),
    path(
        'my-applications/',
        views.my_applications,
        name='my_applications'
    ),

    # Student job and internship tracker
    path(
        'student-tracker/',
        views.student_tracker,
        name='student_tracker'
    ),
    path(
        'student-tracker/edit/<int:opportunity_id>/',
        views.edit_tracked_opportunity,
        name='edit_tracked_opportunity'
    ),
]