from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
###############################################################################

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
###############################################################################

class Digizilla(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    country = models.CharField(max_length=100)
    joining_date = models.DateField()
    tags = models.CharField(max_length=100)
    customers = models.ManyToManyField(Customer)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    notes = models.TextField()
    comments = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name