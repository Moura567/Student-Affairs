from asyncio.windows_events import NULL
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Add(models.Model):
    depart = [
        ('None', 'None'),
        ('Computer science', 'Computer science'),
        ('Operations Research and Decision Support', 'Operations Research and Decision Support'),
        ('Information System', 'Information System'),
        ('Information Technology', 'Information Technology'),
        ('Artificial intelligence', 'Artificial intelligence'),

    ]
    category = [
        ('Female', 'Female'),
        ('Male', 'Male')
    ]
    state = [
        ('Active', 'Active'),
        ('InActive', 'InActive')
    ]

    student_id= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=25)
    GPA= models.DecimalField(max_digits=3,decimal_places=2 )
    level=models.IntegerField(null=False)
    birthday=models.CharField(max_length=16)
    department=models.CharField(max_length=50,choices=depart)
    phonenumber=models.CharField(max_length=12)
    gender=models.CharField(max_length=8,choices=category)
    State=models.CharField(max_length=8,choices=state)
    

    def __str__(self):
        return self.name
