from django.db import models

class School(models.Model):
    name=models.CharField(max_length=20)
    principle=models.CharField(max_length=20)
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name="student")
