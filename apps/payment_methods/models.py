from django.db import models

class PaymentMethod(models.Model):
    id = models.AutoField(
        primary_key=True
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

    date_card = models.CharField(
        max_length=5
    )

    cvv_card = models.CharField(
        max_length=3
    )
    
    owner = models.ForeignKey(
        'users.User',
        verbose_name='Dueño',
        on_delete=models.PROTECT
    )

    REQUIRED_FIELDS = ['type_payment_method', 'number_card', 'date_card', 'cvv_card']

    class Meta:
        verbose_name = "Metodo de Pago"
        verbose_name_plural = "Metodos de Pago"
        ordering = ['id']

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name} {self.number_card}'