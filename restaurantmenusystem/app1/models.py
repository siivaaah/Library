from django.db import models

class Menu(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return self.name

class Menuitem(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="items")
    is_vegetarian=models.BooleanField(default=True)


