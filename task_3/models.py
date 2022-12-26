from django.db import models


# Create your models here.

class Firm(models.Model):
    name_firm = models.CharField(max_length=25)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name_firm, self.address


class Category(models.Model):
    name_category = models.CharField(max_length=25)

    def __str__(self):
        return self.name_category


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    price = models.IntegerField()
    firm_id = models.ForeignKey(Firm, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
