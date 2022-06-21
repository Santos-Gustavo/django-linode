from django.test import TestCase
from django.contrib.auth.models import User
from my_app.models import WorkModel
from django.urls import reverse

# Create your tests here.


class ModelTests(TestCase):
    def test_work_model(self):
        user = User.objects.create_user(username='test_user', password='abc123')
        job = WorkModel.objects.create(
            type_job=1,
            name='Eu',
            profession='Quebra-Galho',
            contact='321654897',
            salary=22,
            language_french=True,
            language_english=True,
            language_dutch=True,
            drivers_license=True,
        )
        response = self.client.get(reverse('my_app:work-construction-page'))
        self.assertEqual(len(response.context['jobs']), 1)
