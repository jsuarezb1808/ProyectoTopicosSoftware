from django.db import models
from django.contrib.auth.models import User

class gafas(models.Model):
    ItemId=models.BigAutoField(primary_key=True)
    ItemName=models.TextField(max_length=255)
    ItemCategory=models.TextField(max_length=255)
    Price=models.IntegerField()


class bodega(models.Model):
    ItemId=models.ManyToManyField(gafas, related_name="bodega_gafas")
    BodegaID=models.BigAutoField(primary_key=True)
    location=models.TextField(max_length=100)
    ItemStock=models.IntegerField()


class wishlist(models.Model):
    WishlistID=models.BigAutoField(primary_key=True)
    User=models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    ItemsId=models.ManyToManyField(gafas , related_name="wishlist_gafas")


class Order(models.Model):
    APROBADA='1'
    PENDIENTE='2'
    DENEGADA='3'

    STATUS_CHOICES=[
        (APROBADA,'aprobada'),
        (PENDIENTE,'pendiente'),
        (DENEGADA,'denegada'),
    ]

    orderID=models.AutoField(primary_key=True)
    status=models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDIENTE,
        )
    address=models.TextField(max_length=255)
    products=models.ManyToManyField (gafas, related_name="orden_gafas")

