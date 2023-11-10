from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

class Classmate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()

    def clean(self):
        if not self.firstname:
            raise ValidationError("First name cannot be empty.")
        if not self.lastname:
            raise ValidationError("Last name cannot be empty.")
        if self.age < 0:
            raise ValidationError("Age cannot be negative.")
        # Add more validation rules as needed

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})
