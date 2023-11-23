from django.db import models


class members(models.Model):
    name = models.CharField(max_length=255)
    phno = models.IntegerField()  # Assuming a string representation for phone number
    package_name = models.CharField(max_length=100)
    m_id = models.CharField(max_length=50, unique=True)  # Assuming a unique member ID
    password = models.CharField(max_length=255)  # Storing passwords as plaintext is not recommended in production


class emplyoee(models.Model):
    name=models.CharField(max_length=25)
    phno=models.IntegerField()
    curr_package=models.IntegerField()
    e_id=models.CharField(max_length=5)
    password=models.CharField(max_length=10)


def __str__(self):
        return self.name
