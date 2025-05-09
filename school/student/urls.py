from django.urls import path
from . import views

urlpatterns = [
    path("admin-dashboard/",views.admin_dashboard,name="admin_dashboard"),
    path("", views.student_list, name='student_list'),
    path("add/", views.add_student, name="add_student"),
    path('students/<int:id>/', views.view_student, name='view_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<str:slug>/', views.delete_student, name='delete_student'),
    path('download-students/', views.download_students_pdf, name='download_students'),
    
]
