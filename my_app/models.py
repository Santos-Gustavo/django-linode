from django.db import models
from django.urls import reverse


class WorkModel(models.Model):
    # blank=True -> Field is not compulsory
    type_job = models.IntegerField()  # 1:Construction, 2:Cleaning, 3:Commerce, 4:HoReCa
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)  # ToDo: use phonenumber_field
    salary = models.IntegerField(blank=True)
    language_french = models.BooleanField(blank=True)
    language_english = models.BooleanField(blank=True)
    language_dutch = models.BooleanField(blank=True)
    drivers_license = models.BooleanField(blank=True)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.type_job} Em {self.date} {self.name} {self.contact}, procura por um {self.profession}, pagando "
            f"€{self.salary} a hora"
        )
