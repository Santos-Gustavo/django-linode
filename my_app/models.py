from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse


class WorkModel(models.Model):
    # blank=True -> Field is not compulsory
    type_job = models.IntegerField()  # 1:Construction, 2:Cleaning, 3:Other
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    contact = models.CharField(max_length=17)
    salary = models.FloatField(validators=[MaxValueValidator(99.99)], blank=True)
    language_french = models.BooleanField(blank=True)
    language_english = models.BooleanField(blank=True)
    language_dutch = models.BooleanField(blank=True)
    drivers_license = models.BooleanField(blank=True)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('my_app:work-item-page', args=(self.id,))

    def __str__(self):
        return (
            f"Tipo {self.type_job}, em {self.date} {self.name} {self.contact}, procura por um {self.profession}, "
            f"pagando €{self.salary} a hora"
        )


class ServiceModel(models.Model):
    # blank=True -> Field is not compulsory
    service_type = models.IntegerField()  # 1:Domestic, 2:Healthy and Beauty, 3:Transport
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    contact = models.CharField(max_length=17)
    price = models.FloatField(blank=True)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='service/%Y/%m/%d/', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('my_app:service-item-page', args=(self.id,))

    def __str__(self):
        return f"Tipo {self.service_type}, em {self.date} {self.title}, {self.id}"
