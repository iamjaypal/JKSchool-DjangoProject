from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
import datetime

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit
# Create your views here.

# def teacher_list(request):
#     teacher_list=Teacher.objects.all()
#     context = {
#         'teacher_list': teacher_list,
#     }
#     return render(request, "teachers/teacher.html", context)

def teacher_list(request):
    query = request.GET.get('q')
    if query:
        teacher_list = Teacher.objects.filter(first_name__icontains=query) | Teacher.objects.filter(last_name__icontains=query)
    else:
        teacher_list = Teacher.objects.all()
    return render(request, 'teachers/teacher.html', {'teacher_list': teacher_list, 'query': query})


def view_teacher(request,id):
    teacher=get_object_or_404(Teacher,teacher_id=id)
    # Print values to check if they exist
    print("Qualification:", teacher.qualification)
    print("Experience Years:", teacher.experience_years)
    print("myteacher",teacher)
    context={
        'teacher' : teacher
    }
    return render(request,'teachers/teacher-details.html',context)

def delete_teacher(request,id):
    teacher=get_object_or_404(Teacher,id=id)
    teacher.delete()
    return redirect("teacher_list")

def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == "POST":
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.teacher_id = request.POST.get('teacher_id')
        teacher.teacher_email = request.POST.get('teacher_email')
        teacher.address = request.POST.get('address')
        teacher.department = request.POST.get('department')
        teacher.specialization = request.POST.get('specialization')
        teacher.experience_years = request.POST.get('experience_years')
        teacher.qualification = request.POST.get('qualification')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.mobile_number = request.POST.get('mobile_number')

        # Handle teacher image update only if a new one is uploaded
        teacher.teacher_image = request.FILES.get('teacher_image') if request.FILES.get('teacher_image') else teacher.teacher_image

        teacher.save()
        return redirect("teacher_list")  # change this if your URL name is different

    return render(request, "teachers/edit-teacher.html", {'teacher': teacher})

def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        teacher_email = request.POST.get('teacher_email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        specialization = request.POST.get('specialization')
        experience_years = request.POST.get('experience_years')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')

        # Convert date strings to date objects
        date_of_birth = datetime.datetime.strptime(request.POST.get('date_of_birth'), "%Y-%m-%d").date()
        joining_date = datetime.datetime.strptime(request.POST.get('joining_date'), "%Y-%m-%d").date()

        mobile_number = request.POST.get('mobile_number')
        teacher_image = request.FILES.get('teacher_image')

        Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            teacher_id=teacher_id,
            teacher_email=teacher_email,
            address=address,
            department=department,
            specialization=specialization,
            experience_years=experience_years,
            qualification=qualification,
            gender=gender,
            date_of_birth=date_of_birth,
            joining_date=joining_date,
            mobile_number=mobile_number,
            teacher_image=teacher_image,
            is_active=True
        )

        messages.success(request, "Teacher added successfully.")
        return redirect('teacher_list')

    return render(request, "teachers/add-teacher.html")



def download_teachers_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="teachers.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 50

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Teacher List")
    y -= 40

    # Table Headers
    p.setFont("Helvetica-Bold", 10)
    headers = ["ID", "Name", "Gender", "DOB", "Joining", "Mobile", "Department"]
    x_positions = [30, 70, 180, 230, 290, 350, 420]

    for i, header in enumerate(headers):
        p.drawString(x_positions[i], y, header)
    y -= 20

    # Table Content
    p.setFont("Helvetica", 9)
    for teacher in Teacher.objects.all():
        if y < 50:
            p.showPage()
            y = height - 50
            p.setFont("Helvetica-Bold", 10)
            for i, header in enumerate(headers):
                p.drawString(x_positions[i], y, header)
            y -= 20
            p.setFont("Helvetica", 9)

        name = f"{teacher.first_name} {teacher.last_name}"
        dob = teacher.date_of_birth.strftime("%d %b %Y") if teacher.date_of_birth else ""
        joining = teacher.joining_date.strftime("%d %b %Y") if teacher.joining_date else ""
        department = teacher.department if teacher.department else "N/A"

        values = [
            str(teacher.teacher_id),
            name,
            teacher.gender,
            dob,
            joining,
            teacher.mobile_number,
            department
        ]

        for i, value in enumerate(values):
            p.drawString(x_positions[i], y, value)
        y -= 18

    p.showPage()
    p.save()
    return response
