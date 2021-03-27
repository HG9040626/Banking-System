from django.db import models

# Create your models here.
class AccountDetail(models.Model):
    acn=models.CharField(max_length=30)
    ifsc=models.CharField(max_length=10)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=30)
    amt=models.IntegerField()
    def __str__(self):
     return str(self.id) +" "+ str(self.name)
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    def __str__(self):
     return str(self.name) +" "+ str(self.email)

