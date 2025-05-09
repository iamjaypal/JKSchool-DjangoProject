from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


# def department_list(request):
#     dep_list=Department.objects.all()
#     return render(request,"departments/department-list.html",{'departments' : dep_list})
    
    
def department_list(request):
    query = request.GET.get('q')
    if query:
        departments = Department.objects.filter(name__icontains=query)
    else:
        departments = Department.objects.all()
    return render(request, 'departments/department-list.html', {'departments': departments, 'query': query})

def download_departments_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="departments.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 50

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Department List")
    y -= 40

    # Headers
    p.setFont("Helvetica-Bold", 10)
    headers = ["ID", "Name of Dep", "Dep Head", "Email", "Contact"]
    x_positions = [30, 70, 200, 350, 460]

    for i, header in enumerate(headers):
        p.drawString(x_positions[i], y, header)
    y -= 20

    p.setFont("Helvetica", 9)
    for dept in Department.objects.all():
        if y < 50:
            p.showPage()
            y = height - 50
            p.setFont("Helvetica-Bold", 10)
            for i, header in enumerate(headers):
                p.drawString(x_positions[i], y, header)
            y -= 20
            p.setFont("Helvetica", 9)

        values = [
            str(dept.id),
            dept.name or "N/A",
            dept.department_head or "N/A",
            dept.head_email or "N/A",
            dept.contact_number or "N/A"
        ]

        for i, value in enumerate(values):
            p.drawString(x_positions[i], y, value)
        y -= 18

    p.showPage()
    p.save()
    return response

def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department_head = request.POST.get('department_head')
        head_email = request.POST.get('head_email')
        contact_number = request.POST.get('contact_number')

        Department.objects.create(
            name=name,
            department_head=department_head,
            head_email=head_email,
            contact_number=contact_number
        )
        return redirect('department_list') 
    return render(request, 'departments/add-department.html')

 
def edit_department(request,id):
    department=get_object_or_404(Department,id=id)
    
    if request.method=="POST":
        department.name=request.POST.get('name')
        department.head_email=request.POST.get('head_email')
        department.department_head=request.POST.get('department_head')
        department.contact_number=request.POST.get('contact_number')
        department.save()
        return redirect("department_list")
    
    return render(request,"departments/edit-department.html",{"department" : department}) 

   
        
def delete_department(request,id):
    dept=get_object_or_404(Department,id=id)
    dept.delete()
    return redirect("department_list")


# def subjects_list(request):
#     subjects_list=Subject.objects.all()
#     return render(request,"subjects/subjects-list.html",{"subjects":subjects_list})
    

def subjects_list(request):
    query = request.GET.get('q')
    if query:
        subjects = Subject.objects.filter(name__icontains=query)
    else:
        subjects = Subject.objects.all()
    
    context = {
        'subjects': subjects,
        'query': query,
    }
    return render(request, 'subjects/subjects-list.html', context)

 
def add_subject(request):
    if request.method=="POST":
        name=request.POST.get('name')
        department_id=request.POST.get('department')
        department=Department.objects.get(id=department_id)
        
        Subject.objects.create(name=name,department=department)
        return redirect("subjects_list")
    departments=Department.objects.all()
    return render(request,"subjects/add-subject.html",{"departments":departments})
      
    
def edit_subject(request,id):
    subject=get_object_or_404(Subject,id=id)
    departments=Department.objects.all()
    if request.method=="POST":
          subject.name=request.POST.get('name')
          dep_id=request.POST.get('department')
          subject.department=Department.objects.get(id=dep_id)
          subject.save()
          return redirect("subjects_list")
      
    return render(request,"subjects/edit-subject.html",{'subject':subject, 'departments': departments})

def delete_subject(request,id):
    subject=get_object_or_404(Subject,id=id)
    subject.delete()
    return redirect("subjects_list")


    
def download_subjects_pdf(request):
    # Create the HttpResponse object with PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="subjects.pdf"'

    # Create the PDF object using canvas
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 50

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Subject List")
    y -= 40

    # Table Headers
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "ID")
    p.drawString(100, y, "Subject Name")
    p.drawString(300, y, "Department")
    y -= 20

    # Table Content
    p.setFont("Helvetica", 12)
    for subject in Subject.objects.all():
        if y < 50:
            p.showPage()
            y = height - 50
        p.drawString(50, y, str(subject.id))
        p.drawString(100, y, subject.name)
        p.drawString(300, y, subject.department.name)
        y -= 20

    p.showPage()
    p.save()
    return response