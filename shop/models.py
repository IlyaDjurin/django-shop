from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone



class Kategor(models.Model):
    kategory_name = models.CharField(max_length=200, db_index=True)
    kategory_slug = models.SlugField(max_length=200, db_index=True, unique=True)
    kategory_info = models.TextField(blank=True, verbose_name="Описание")
    kategory_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение категории")

    class Meta:
        ordering = ['kategory_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.kategory_slug])

    def __str__(self):
        return self.kategory_name




class Tovar(models.Model):
    kategory_id = models.ForeignKey(Kategor, related_name='tovars', verbose_name="Категория")
    tovar_name = models.CharField(max_length=200, db_index=True, verbose_name="Название(указать обязательно,к примеру 'Meizu')")
    tovar_slug = models.SlugField(max_length=200, db_index=True, unique=True)
    tovar_info = models.TextField(blank=True, verbose_name="Описание")
    tovar_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    tovar_made = models.CharField(max_length=200)
    tovar_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    tovar_url = models.CharField(max_length=200)
    tovar_stock = models.PositiveIntegerField(verbose_name="На складе")
    tovar_available = models.BooleanField(default=True, verbose_name="Доступен")
    tovar_created = models.DateTimeField(auto_now_add=True)
    tovar_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        ordering = ['tovar_name']
        index_together = [
            ['id', 'tovar_slug']
        ]

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.tovar_slug])

    def __str__(self):
        return self.tovar_name


class Tovar_inphoto(models.Model):
    tovar_id = models.ForeignKey(Tovar, related_name='haraktertovar', verbose_name="Товар")
    tovarinphoto_slug = models.SlugField(max_length=200, db_index=True, unique=True)
    tovarinphoto_info = models.TextField(blank=True, verbose_name="Описание")
    tovarinphoto_proizv = models.CharField(max_length=200 , verbose_name="Производитель(фирма)")
    tovarinphoto_diagon = models.CharField(max_length=200, verbose_name="Диагональ")
    tovarinphoto_ram = models.CharField(max_length=200, verbose_name="Оперативная память")
    tovarinphoto_akb = models.CharField(max_length=200, verbose_name="Емкость акумулятора")
    tovarinphoto_osnkamera = models.CharField(max_length=200, verbose_name="Основная камера Мпс")
    tovarinphoto_opsystem = models.CharField(max_length=200, verbose_name="Операционная система")
    tovarinphoto_color = models.CharField(max_length=200, verbose_name="Цвет товара")
    tovarinphoto_cpu = models.CharField(max_length=200, verbose_name="Процессор")
    tovarinphoto_razreshenie = models.CharField(max_length=200, verbose_name="Разрешение дисплея")
    tovarinphoto_frontkamera = models.CharField(max_length=200, verbose_name="Фронтальная камера Мпс")
    tovarinphoto_scaner = models.CharField(max_length=200, verbose_name="Сканер отпечатка пальца")
    tovarinphoto_3g = models.CharField(max_length=200, verbose_name="Наличие 3g LTE GPRS технологии")
    tovarinphoto_gps = models.CharField(max_length=200, verbose_name="Поддерживаемые системы навигации,спутники")
    tovarinphoto_matrix = models.CharField(max_length=200, verbose_name="Тип матрицы")
    tovarinphoto_sim = models.CharField(max_length=200, verbose_name="Количество сим-карт")

    class Meta:
        verbose_name = 'характеристику'
        verbose_name_plural = 'Характеристики'
        ordering = ['tovarinphoto_proizv']
        index_together = [
            ['id', 'tovarinphoto_slug']
        ]

    def __str__(self):
        return self.tovarinphoto_info


class Tovar_img(models.Model):
    tovarinphoto_id = models.ForeignKey(Tovar_inphoto, related_name='phototovar', verbose_name="Фото товара")
    tovar_name = models.CharField(max_length=200, db_index=True, verbose_name="Название товара", default=None)
    tovar_image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    tovar_image1 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара1")
    tovar_image2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара2")
    tovar_image3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара3")
    tovar_info3 = models.TextField(blank=True, verbose_name="Описание3")
    tovar_image4 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара4")
    tovar_info4 = models.TextField(blank=True, verbose_name="Описание4")
    tovar_image5 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара5")
    tovar_info5 = models.TextField(blank=True, verbose_name="Описание5")
    tovar_image6 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара6")
    tovar_image7 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара7")
    tovar_image8 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара8")
    tovar_image9 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара9")
    tovar_image10 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара10")
    tovar_image11 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара11")
    tovar_video = models.CharField(max_length=200, blank= True)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.tovar_name








