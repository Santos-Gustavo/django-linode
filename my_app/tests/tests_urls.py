from django.urls import reverse
from .test_work_base import WorkTestsBase
# Create your tests here.


class URLTests(WorkTestsBase):
    def test_home_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:index-page'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_status_code_200_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:login-page'))
        self.assertEqual(response.status_code, 200)

    def test_success_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:success-page'))
        self.assertEqual(response.status_code, 200)

    def test_success_account_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:success-account-page'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:signup-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:work-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_construction_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:work-construction-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_construction_form_view_status_code_200_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:work-construction-form-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_construction_form_view_status_code_302_OK(self):
        response = self.client.get(reverse('my_app:work-construction-form-page'))
        self.assertEqual(response.status_code, 302)

    def test_work_cleaning_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:work-cleaning-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_cleaning_form_view_status_code_200_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:work-cleaning-form-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_cleaning_form_view_status_code_302_OK(self):
        response = self.client.get(reverse('my_app:work-cleaning-form-page'))
        self.assertEqual(response.status_code, 302)

    def test_work_other_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:work-other-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_other_form_view_status_code_200_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:work-other-form-page'))
        self.assertEqual(response.status_code, 200)

    def test_work_other_form_view_status_code_302_OK(self):
        response = self.client.get(reverse('my_app:work-other-form-page'))
        self.assertEqual(response.status_code, 302)

    def test_service_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_form_view_status_code_200_OK(self):
        self.make_user()
        response = self.client.get(reverse('my_app:service-form-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_form_view_status_code_302_OK(self):
        response = self.client.get(reverse('my_app:service-form-page'))
        self.assertEqual(response.status_code, 302)

    def test_service_domestic_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-domestic-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_healthy_beauty_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-healthy-beauty-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_transport_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-transport-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_food_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-food-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_technic_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-technic-page'))
        self.assertEqual(response.status_code, 200)

    def test_service_other_view_status_code_200_OK(self):
        response = self.client.get(reverse('my_app:service-other-page'))
        self.assertEqual(response.status_code, 200)
