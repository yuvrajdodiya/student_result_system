from django.db import models

# Create your models here.

class Student(models.Model):

    student_name = models.CharField(max_length=50)

    student_phone = models.CharField(max_length=11)

    student_email = models.EmailField()

    student_aadhar = models.ImageField(upload_to='addar/')

    student_photo = models.ImageField(upload_to='students/')

    c = models.IntegerField()
    cpp = models.IntegerField()
    java = models.IntegerField()
    python = models.IntegerField()
    html = models.IntegerField()
    css = models.IntegerField()
    sql = models.IntegerField()
    
    def __str__(self):
        return self.student_name