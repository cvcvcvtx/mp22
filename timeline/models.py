
from django.db import models
from django.conf import settings
from contacts.models import Contact 
from deals.models import Deal        

class ActionLog(models.Model):
    """Модель для логирования действий пользователей"""
    class ActionType(models.TextChoices):
        CREATED = 'CREATED', 'Создал'
        UPDATED = 'UPDATED', 'Обновил'
        DELETED = 'DELETED', 'Удалил'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Пользователь"
    )
    action_type = models.CharField("Тип действия", max_length=10, choices=ActionType.choices)
    record_info = models.CharField("Информация о записи", max_length=255)
    timestamp = models.DateTimeField("Время", auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.action_type} {self.record_info} в {self.timestamp}"

class Activity(models.Model):
    """Модель активности (звонок, встреча, email)"""
    class ActivityType(models.TextChoices):
        CALL = 'CALL', 'Звонок'
        MEETING = 'MEETING', 'Встреча'
        EMAIL = 'EMAIL', 'Email'
        NOTE = 'NOTE', 'Заметка'

    type = models.CharField("Тип активности", max_length=10, choices=ActivityType.choices)
    notes = models.TextField("Заметки")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='activities',
        verbose_name="Кем создано"
    )
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='activities')
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, related_name='activities', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display()} с {self.contact}"