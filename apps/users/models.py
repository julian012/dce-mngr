from django.db import models

from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class User(AbstractUser):

    id = models.AutoField(
        primary_key=True
    )

    first_name = models.CharField(
        'Nombres',
        max_length=150
    )

    last_name = models.CharField(
        'Apellido',
        max_length=150
    )

    CARD = 1
    IDENTIFICATION_CARD = 2
    IMMIGRATION_CARD = 3
    PASSPORT = 4
    OTHER = 5
    type_identification = models.PositiveSmallIntegerField(
        'Tipo de identificación',
        choices=(
            (CARD, 'Cédula de ciudadanía'),
            (IDENTIFICATION_CARD, 'Tarjeta de identidad'),
            (IMMIGRATION_CARD, 'Cédula de extranjería'),
            (PASSPORT, 'Pasaporte'),
            (OTHER, 'Otro'),
        ),
        default=CARD,
    )

    identification = models.CharField(
        'Identificación',
        max_length=11
    )


    cellphone = models.CharField(
        'Número telefónico',
        max_length=50,
        null=True,
        blank=True
    )

    username = models.CharField(
        'Username',
        max_length=150,
        unique=True
    )

    email = models.EmailField(
        'Correo',
        unique=True
    )

    password = models.CharField(
        'Contraseña',
        max_length=120,
    )

    username = None

    ACTIVE = 1
    INACTIVE = 2
    state = models.PositiveSmallIntegerField(
        'Estado',
        choices=(
            (ACTIVE, 'Activo'),
            (INACTIVE, 'Inactivo')
        ),
        default=ACTIVE
    )

    REQUIRED_FIELDS = ['first_name', 'last_name', 'type_identification', 'identification']

    USERNAME_FIELD = 'email'

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def get_username(self):
        return self.email

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    objects = UserManager()
   
