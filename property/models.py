from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):

    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    is_new_building = models.BooleanField(
        'Новое здание',
        null=True,
        blank=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    class Meta:
        verbose_name = 'Квартиру'
        verbose_name_plural = 'Квартиры'


class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Кто жаловался')
    flat = models.ForeignKey('Flat', on_delete=models.CASCADE, verbose_name='Квартира, на которую пожаловались')
    text = models.TextField()

    def __str__(self):
        return f'{self.flat.town},{self.flat.address}'

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class Owner(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО владельца', db_index=True)
    pure_phonenumber = PhoneNumberField(verbose_name='Нормализованный номер владельца', db_index=True)
    flat = models.ManyToManyField('Flat', related_name='owners', verbose_name='Квартиры в собственности', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
