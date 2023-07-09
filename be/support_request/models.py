from django.db import models

# Create your models here.


class SupportRequest(models.Model):
    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['-created_at',]

    NEW = 'new'
    IN_WORK = 'proc'
    REJECTED = 'rjct'
    CLOSED = 'clsd'
    STATUSES = [
        (NEW, 'Открытая'),
        (IN_WORK, 'Ожидает подтверждения'),
        (REJECTED, 'Неоценённая'),
        (CLOSED, 'Закрытая'),
    ]

    number = models.CharField('№ заявки', max_length=12, unique=True, db_index=True)
    created_at = models.DateTimeField('добавлено', auto_now_add=True)
    short_description = models.CharField('краткое описание', max_length=255)
    author = models.CharField('заявитель', max_length=255)
    status = models.CharField('статус', max_length=4, choices=STATUSES, default=NEW)
    decision = models.CharField('решение', max_length=255, blank=True, null=True)
    state = models.CharField('состояние', max_length=255, default='Состояние 0')
    deadline = models.DateTimeField('крайний срок', null=True, blank=True)
    closed = models.BooleanField('закрыто', default=False)
    description = models.TextField('подробное описание')
    contact = models.CharField('контактное лицо', max_length=255, blank=True, null=True)
