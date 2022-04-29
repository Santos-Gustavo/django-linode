from django.db import models


class WorkModel(models.Model):
    # blank=True -> Field is not required
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    contact = models.IntegerField()
    language_french = models.BooleanField(blank=True)
    salary = models.IntegerField(blank=True)
    language_english = models.BooleanField(blank=True)
    language_dutch = models.BooleanField(blank=True)
    drivers_license = models.BooleanField(blank=True)
    description = models.TextField(max_length=1000, blank=True)
    date = models.DateField()
    # ToDo: add date form was created

    def __str__(self):
        return (
            f"{self.name}, procurando {self.profession}, "
            f"Tem  que falar, "
            f"{self.description}"
                )
