from django.urls import path
from . import views

urlpatterns = [
    path("",views.teacher_list, name='teacher_list'),
    path("add/",views.add_teacher,name='add_teacher'),
    path("view/<int:id>",views.view_teacher,name='view_teacher'),
    path("edit/<int:id>",views.edit_teacher,name="edit_teacher"),
    path("delete/<int:id>",views.delete_teacher,name='delete_teacher'),
    path('teachers/download/', views.download_teachers_pdf, name='download_teachers_pdf'),

]
