

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


class Stage(models.Model):
    """Модель для кастомных этапов сделки"""
    name = models.CharField("Название этапа", max_length=100, unique=True)
    order = models.PositiveIntegerField("Порядок", default=0, help_text="Для сортировки на канбан-доске")
    color = models.CharField("Цвет в HEX", max_length=7, default="#FFFFFF", help_text="Например, #FF0000")

    class Meta:
        ordering = ['order'] 

    def __str__(self):
        return self.name

class Deal(models.Model):
    """Модель сделки (ОБНОВЛЕННАЯ)"""
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