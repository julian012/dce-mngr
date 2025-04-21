from django.db import models
from django.utils.text import slugify

class Product(models.Model):

    def get_upload_path(self, filename):
        filename = filename.split('.')
        extension = filename.pop()
        name = ''.join(filename)
        res = f'productos/{slugify(name)}.{extension}'
        return res

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        'Nombre',
        max_length=150,
        blank=False
    )

    description = models.TextField(
        'Descripción',
        blank=False
    )

    image = models.ImageField(
        'Imagen',
        upload_to=get_upload_path,
        max_length=500,
        blank=False
    )

    is_avaliable = models.BooleanField(
        'Esta activo',
        default=True
    )

    product_stock =  models.PositiveBigIntegerField(
        'Cantidad',
        blank=False,
        default=0
    )

    product_price = models.IntegerField(
        'Precio',
        default=0,
        blank=False
    )

    def __str__(self):
        return f'{self.name} - {self.product_price}'
