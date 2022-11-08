from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Sensor(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Название')
    description = models.CharField(max_length=40, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
        verbose_name='Датчик',
    )
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(-50), MaxValueValidator(50)],
        verbose_name='Температура',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
