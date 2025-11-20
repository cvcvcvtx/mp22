
from django.db import models
from django.conf import settings
from contacts.models import Contact 
from deals.models import Deal       

class Task(models.Model):
    """Модель задачи"""
    class StatusChoices(models.TextChoices):
        TODO = 'TODO', 'К выполнению'
        DONE = 'DONE', 'Выполнена'

    title = models.CharField("Название задачи", max_length=255)
    description = models.TextField("Описание", blank=True)
    due_date = models.DateTimeField("Срок выполнения")
    status = models.CharField("Статус", max_length=10, choices=StatusChoices.choices, default=StatusChoices.TODO)
    
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="Исполнитель"
    )
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True, verbose_name="Сделка")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True, verbose_name="Контакт")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title