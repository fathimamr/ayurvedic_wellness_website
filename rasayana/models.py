from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    SPECIALIST_CHOICES = [
        ('Chief Physician', 'DR. V MADHAVACHANDRAN'),
        ('Consulting Physician', 'DR. JINTU JOSE'),
        ('General', 'General Consultation'),
    ]

    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    specialist = models.CharField(max_length=50, choices=SPECIALIST_CHOICES)
    preferred_date = models.DateField()
    phone = models.CharField(max_length=15)
    concerns = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name