from django.db import models
from django.forms import ModelForm
# Create your models here.


class Brand (models.Model):
    idBrand = models.CharField(unique=True, primary_key=True)
    nameBrand = models.TextField()
    descriptionBrand = models.TextField(default="This is a famous brand")


class Product (models.Model):
    idProduct = models.CharField(unique=True, primary_key=True)
    name = models.TextField(max_length=200)
    description = models.TextField(default="This is a product")
    price = models.IntegerField()
    numberRemain = models.IntegerField()
    createdAt = models.DateTimeField("Time create")
    updatedAt = models.DateTimeField("Time update")
    avatar = models.FileField(upload_to="avatar/")
    idBrandProduct = models.ForeignKey(Brand, on_delete=models.CASCADE)
