from django.test import TestCase
from django.contrib.auth.models import User
from my_app.models import WorkModel

# Create your tests here.


class URLTests(TestCase):
    def setUp(self):
        pass

    def test_check_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_check_work_page(self):
        response = self.client.get('work/')
        self.assertEqual(response.status_code, 200)

    def test_user_exists(self):
        user_a = User.objects.create(
            username='abc', password='12345678'
        )
        work_post = WorkModel.objects.create(
            type_job=1,
            name='test',
            profession='test_profession',
            contact='0123456'
        )

