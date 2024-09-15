from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.price <= 0:
            raise ValidationError('Price must be a positive number.')
        if not self.name:
            raise ValidationError('Name cannot be empty.')

    def __str__(self):
        return self.name
