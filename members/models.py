from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    DateOfJoining = models.DateField(null=True)
    designation = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"