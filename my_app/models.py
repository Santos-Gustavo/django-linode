from django.db import models


class WorkModel(models.Model):
    name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    freelancer = models.CharField(max_length=3)
    language = models.CharField(max_length=12)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return (
            f"{self.name}, procurando {self.profession}, "
            f"Freelancer: {self.freelancer}, "
            f"Tem  que falar {self.language}, "
            f"{self.description}"
                )
