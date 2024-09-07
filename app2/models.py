from django.db import models


# Create your models here.
class Student(models.Model):
    stu_name =  models.CharField(max_length=200)
    stu_image =  models.ImageField(upload_to="image")
    stu_resume =  models.FileField(upload_to="file")