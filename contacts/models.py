from django.db import models
from django.conf import settings 


class Contact(models.Model):
    """Модель контакта (клиента)"""
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Email", max_length=254, unique=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    company = models.CharField("Компания", max_length=150, blank=True)
    
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contacts',
        verbose_name="Ответственный менеджер"
    )
    
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"