from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()
    language=models.CharField(max_length=20)
    year= models.IntegerField()
    image=models.ImageField(upload_to="image")

    def __str__(self):
        return self.title

