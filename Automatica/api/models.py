from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Worker(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    phone_number = models.CharField(_('Phone_number'),
                                    unique=True, max_length=255,
                                    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Worker')
        verbose_name_plural = _('Workers')


class Store(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    worker = models.ForeignKey('api.Worker', verbose_name=_('Worker'),
                               on_delete=models.CASCADE, related_name='stores_worker')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')


class Visit(models.Model):
    date = models.DateTimeField(_('Vist date'), auto_now_add=True)
    store = models.ForeignKey('api.Store', verbose_name=_('Store'),
                              on_delete=models.CASCADE, related_name='visits_store')

    latitude = models.FloatField(_('latitude'), validators=[MinValueValidator(limit_value=-90),
                                                            MaxValueValidator(limit_value=90)])
    longitude = models.FloatField(_('longitude'))

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = _('Visit')
        verbose_name_plural = _('Visits')
