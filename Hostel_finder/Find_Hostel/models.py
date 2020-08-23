from django.db import models

# Create your models here.
class Hostels(models.Model):
    hostel_id=models.AutoField
    hostel_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to="Find_Hostel/images",default="")
    rent=models.IntegerField(default=0)


    def __str__(self):
        return self.hostel_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70, default="")
    phone=models.CharField(max_length=70, default="")
    desc=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


    
