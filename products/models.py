from django.db import models
from django.conf import settings


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=20)
    category_description = models.TextField()
    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    dateAdded = models.DateTimeField()

    def __str__(self):
        return self.name

