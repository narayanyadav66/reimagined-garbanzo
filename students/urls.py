
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_student, name='add_student'),
    path(
        'edit/<int:student_id>/',
        views.edit_student,
        name='edit_student'
    ),
    path(
        'delete/<int:student_id>/',
        views.delete_student,
        name='delete_student'
    ),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/excel/', views.export_excel, name='export_excel'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='students/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
