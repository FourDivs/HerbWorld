from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    profile_image = models.ImageField(
        null=True, upload_to="media/herbworldapp/images/", default="neuroly/profile_images/default.jpg")

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nursery_name = models.CharField(max_length=100, default="none")
    phone = models.CharField(max_length=12)
    profile_image = models.ImageField(
        null=True, upload_to="herbworldapp/images/", default="herbworldapp/images/")

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    product_id = models.CharField(max_length=50)
    nursery_id = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    product_image = models.ImageField(
        null=True, upload_to="herbworldapp/images/", default="herbworldapp/images/M1_1.png")

    def __str__(self):
        return self.product_id


class Order(models.Model):
    order_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    nursery_id = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=50, default='none')
    order_total = models.IntegerField(default=0)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.order_id

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length = 70)
    message = models.CharField(max_length = 500)

    def __str__(self):
        return self.email
