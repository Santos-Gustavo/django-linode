from django.test import TestCase
from django.contrib.auth.models import User
from my_app.models import WorkModel, ServiceModel
from django.test.client import Client

# Create your tests here.


class WorkTestsBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_user(self):
        self.client = Client()
        User.objects.create_user(username='test_user', password='abc123')
        return self.client.login(username='test_user', password='abc123')

    @staticmethod
    def make_job(type_job=1):
        return WorkModel.objects.create(
            type_job=type_job,
            name='work_name_test',
            profession='profession test',
            author_id=1,
            contact='+32 123 456',
            salary=22,
            language_french=True,
            language_english=True,
            language_dutch=True,
            drivers_license=True,
        )

    @staticmethod
    def make_service(service_type):
        return ServiceModel.objects.create(
            service_type=service_type,
            title='service_title',
            author_id=1,
            contact='+32 123 456',
            price=5000
        )
