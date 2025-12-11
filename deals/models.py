
from django.db import models
from django.conf import settings
from contacts.models import Contact 

class Stage(models.Model):
    """Модель для кастомных этапов сделки"""
    name = models.CharField("Название этапа", max_length=100, unique=True)
    order = models.PositiveIntegerField("Порядок", default=0, help_text="Для сортировки на канбан-доске или чего то подобного")
    color = models.CharField("Цвет в HEX", max_length=7, default="#FFFFFF")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Deal(models.Model):
    """Модель сделки"""
    title = models.CharField("Название сделки", max_length=200)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='deals', verbose_name="Контакт")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='deals',
        verbose_name="Ответственный"
    )
    stage = models.ForeignKey(
        Stage,
        on_delete=models.PROTECT,
        related_name='deals',
        verbose_name="Этап сделки",
        null=True,
        blank=True
    )
    value = models.DecimalField("Сумма сделки", max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return self.title