from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    teacher_email = models.EmailField(max_length=20,null=True)
    address = models.TextField()
    department = models.CharField(max_length=100,null=True) 
    specialization = models.CharField(max_length=100,null=True)
    experience_years = models.CharField(max_length=10,null=True)
    qualification = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField(null=True)            
    joining_date = models.DateField(null=True)
    mobile_number = models.CharField(max_length=15,null=True)
    teacher_image = models.ImageField(upload_to='teachers/', blank=True)
    is_active = models.BooleanField(default=True)   

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"
