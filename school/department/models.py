from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)  
    department_head = models.CharField(max_length=255, null=True, blank=True)  
    head_email = models.EmailField(null=True, blank=True)  
    contact_number = models.CharField(max_length=20, null=True, blank=True)  

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255) 
    department = models.ForeignKey(Department, related_name='subjects', on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
