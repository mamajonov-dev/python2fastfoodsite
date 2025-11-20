from django.db import models
from django.contrib.auth.models import User

class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    def __str__(self):
        return self.name
class KarzinkaModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def umumiysuma(self):
        summa = self.product.price * self.count
        return summa

    def __str__(self):
        return self.product.name


class OrderModel(models.Model):
    karzikna = models.ForeignKey(KarzinkaModel, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    qabul_qiluvchi = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qabul_qiluvchi