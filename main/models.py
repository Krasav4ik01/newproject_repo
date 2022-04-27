from tabnanny import verbose
from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import AbstractUser

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)




# Create your models here.
class Db(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(blank=False)

    class Meta:
        verbose_name = "Мақала"
        verbose_name_plural="Мақалалар"
        ordering = ["title","content"]

    def __str__(self):
        return self.title
    
    def get_num(self):
        return 5

    def get_title(self):
        return "MyName"

class Login(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    number = models.IntegerField(validators=[MinValueValidator(10000),
                                       MaxValueValidator(100000000000)])
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
         return self.name




    


class Sport(models.Model):
    name = models.CharField( max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    

class MenPrize(models.Model):
    fullnames = models.CharField(max_length=50)
    medaltype= models.CharField(max_length=50)

class Men(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)

class Women(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)




class Articles(models.Model):
    title = models.CharField('Name', max_length=250)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Statya')

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новость'


class Mvideo(models.Model):
    mcountry = models.CharField(max_length=50)
    mtext = models.TextField(max_length=5000)
    msportsmen=models.CharField(max_length=50)
    mcaption = models.CharField(max_length=100)
    mvideo = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.mcaption