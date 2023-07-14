from django.db import models

# Create your models here.
class Student(models.Model):
    srn=models.CharField(max_length=8)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
        
        