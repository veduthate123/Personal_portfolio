from django.db import models


class registerinfo(models.Model):
    
    ROLE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    ]
    
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=255,choices=ROLE_CHOICES,null=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Profile_Picture = models.ImageField(upload_to="images",max_length=350,default="")
    Username = models.CharField(max_length=50)
    Email_Id = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Address_Line1 = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=50)
    
    def  __str__(self):
        return self.First_Name
    
    