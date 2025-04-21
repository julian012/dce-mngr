from django.db import models

class Buyout(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    buyer = models.ForeignKey(
        'users.User',
        verbose_name='Comprador',
        on_delete=models.PROTECT
    )

    total_price = models.IntegerField(
        'Precio total',
        blank=False
    )

    buyout_date = models.DateTimeField(
        'Fecha de compra',
        auto_now_add=True
    )

    DEBIT_CARD = 1
    CREDIT_CARD = 2
    type_payment_method = models.PositiveSmallIntegerField(
        'Tipo de Tarjeta',
        choices=(
            (DEBIT_CARD, 'Tarjeta Debito'),
            (CREDIT_CARD, 'Tarjeta de Credito'),
        ),
        default=DEBIT_CARD,
    )

    number_card = models.CharField(
        'Numero de Tarjeta',
        max_length=16
    )

    def __srt__(self):
        return f'{self.buyout_date} {self.buyer.first_name} {self.total_price}'
    
class BuyoutProduct(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    buyout = models.ForeignKey(
        'buyouts.Buyout',
        verbose_name='Compra',
        on_delete=models.PROTECT
    )

    product = models.ForeignKey(
        'products.Product',
        verbose_name='Producto',
        on_delete=models.PROTECT
    )

    quantity = models.PositiveSmallIntegerField(
        'Cantidad',
        blank=False
    )

    product_price = models.IntegerField(
        'Precio por producto',
        blank=False
    )

    def __str___(self):
        return f'{self.buyout.id} {self.product.name} {self.quantity} {self.product_price}'
