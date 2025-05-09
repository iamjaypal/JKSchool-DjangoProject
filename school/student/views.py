from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

# Create your views here.

def admin_dashboard(request):
    return render(request,"Home/index.html")


def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        # Retrieve parent data from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # save parent information
        parent = Parent.objects.create(
            father_name= father_name,
            father_occupation= father_occupation,
            father_mobile= father_mobile,
            father_email= father_email,
            mother_name= mother_name,
            mother_occupation= mother_occupation,
            mother_mobile= mother_mobile,
            mother_email= mother_email,
            present_address= present_address,
            permanent_address= permanent_address
        )

        # Save student information
        student = Student.objects.create(
            first_name= first_name,
            last_name= last_name,
            student_id= student_id,
            gender= gender,
            date_of_birth= date_of_birth,
            student_class= student_class,
            religion= religion,
            joining_date= joining_date,
            mobile_number = mobile_number,
            admission_number = admission_number,
            section = section,
            student_image = student_image,
            parent = parent
        )
        # create_notification(request.user, f"Added Student: {student.first_name} {student.last_name}")
        messages.success(request, "Student added Successfully")
        return redirect("student_list")

  

    return render(request,"students/add-student.html")



def student_list(request):
    query = request.GET.get('q')
    if query:
        student_list = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    else:
        student_list = Student.objects.all()

    return render(request, 'students/students.html', {'student_list': student_list, 'query': query})


# def student_list(request):
#     student_list = Student.objects.select_related('parent').all()
#     context = {
#         'student_list': student_list,
#     }
#     return render(request, "students/students.html", context)


def edit_student(request,id):
    student = get_object_or_404(Student, id=id)
    parent = student.parent if hasattr(student, 'parent') else None
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')  if request.FILES.get('student_image') else student.student_image

        # Retrieve parent data from the form
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()

#  update student information

        student.first_name= first_name
        student.last_name= last_name
        student.student_id= student_id
        student.gender= gender
        student.date_of_birth= date_of_birth
        student.student_class= student_class
        student.religion= religion
        student.joining_date= joining_date
        student.mobile_number = mobile_number
        student.admission_number = admission_number
        student.section = section
        student.student_image = student_image
        student.save()
        # create_notification(request.user, f"Added Student: {student.first_name} {student.last_name}")
        
        return redirect("student_list")
    return render(request, "students/edit-student.html",{'student':student, 'parent':parent} )



def view_student(request, id):
    student = get_object_or_404(Student, student_id = id)
    context = {
        'student': student
    }
    return render(request, "students/student-details.html", context)

@csrf_protect
def delete_student(request,slug):
    if request.method == "POST":
        student = get_object_or_404(Student, slug=slug)
        print("Student deleted ",student)
        student.delete()
        # create_notification(request.user, f"Deleted student: {student_name}")
        return redirect ('student_list')
    return HttpResponseForbidden()

from django.http import HttpResponse




def download_students_pdf(request):
    # Create PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    # Landscape page
    p = canvas.Canvas(response, pagesize=landscape(A4))
    width, height = landscape(A4)
    x_offset = 40
    y = height - 50

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(x_offset, y, "Student List")
    y -= 30

    # Column Titles
    p.setFont("Helvetica-Bold", 10)
    headers = ["ID", "Name", "Class", "DOB", "Father / Mother", "Mobile", "Address"]
    positions = [x_offset, 80, 180, 260, 340, 460, 530]

    for i in range(len(headers)):
        p.drawString(positions[i], y, headers[i])

    y -= 20
    p.setFont("Helvetica", 9)

    # Table rows
    students = Student.objects.all()
    for student in students:
        if y < 50:
            p.showPage()
            p.setFont("Helvetica-Bold", 10)
            for i in range(len(headers)):
                p.drawString(positions[i], height - 50, headers[i])
            y = height - 70
            p.setFont("Helvetica", 9)

        name = f"{student.first_name} {student.last_name}"
        parent = f"{student.parent.father_name} / {student.parent.mother_name}"
        dob = student.date_of_birth.strftime("%d %b %Y")
        address = student.parent.present_address

        values = [
            str(student.student_id),
            name,
            student.student_class,
            dob,
            parent,
            student.mobile_number,
            address[:40]  # truncate address if long
        ]

        for i in range(len(values)):
            p.drawString(positions[i], y, values[i])
        y -= 18

    p.showPage()
    p.save()
    return response