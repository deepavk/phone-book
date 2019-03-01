from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'email',]),
        ]

    def __str__(self):
        return self.email
