from django.urls import path
from . import views

urlpatterns = [
    path("",views.department_list, name='department_list'),
    path("add/",views.add_department,name='add_department'),
    path("edit/<int:id>",views.edit_department,name="edit_department"),
    path("delete/<int:id>",views.delete_department,name='delete_department'),
    path("subjects-list/",views.subjects_list,name='subjects_list'),
    path("add-subject/",views.add_subject,name='add_subject'),
    path("edit-subject/<int:id>",views.edit_subject,name='edit_subject'),
    path("delete-subject/<int:id>",views.delete_subject,name="delete_subject"),
    path('download-subjects/', views.download_subjects_pdf, name='download_subjects'),
    path('departments/download/', views.download_departments_pdf, name='download_departments_pdf'),

]