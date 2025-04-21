from django.db import models

class ShoppingCart(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    user = models.ForeignKey(
        'users.User',
        verbose_name='Usuario',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        'products.Product',
        verbose_name='Producto',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveBigIntegerField(
        'Cantidad',
        blank=False
    )

    def __str__(self):
        return f'{self.user.first_name} {self.product.name} {self.quantity}'
