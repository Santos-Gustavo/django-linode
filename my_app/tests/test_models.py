from django.test import TestCase
from django.contrib.auth.models import User
from my_app.models import WorkModel
from django.urls import reverse
from .test_work_base import WorkModelTests
# Create your tests here.


class ViewsTests(WorkModelTests):
    def test_work_model_loads_in_page_template(self, type_job=0, template_name='my_app:work-page'):
        self.make_job(type_job=type_job)
        response = self.client.get(reverse(template_name))
        content = response.content.decode('utf-8')
        response_context_job = response.context['jobs']

        # Check if post appears in page
        self.assertIn('work_name_test', content)
        self.assertIn('profession test', content)
        self.assertIn('+32 123 456', content)
        self.assertEqual(len(response_context_job), 1)
    
    def test_work_construction_model_loads_in_page(self):
        self.test_work_model_loads_in_page_template(type_job=1, template_name='my_app:work-construction-page')

    def test_work_cleaning_model_loads_in_page(self):
        self.test_work_model_loads_in_page_template(type_job=2, template_name='my_app:work-cleaning-page')
        
    def test_work_other_model_loads_in_page(self):
        self.test_work_model_loads_in_page_template(type_job=3, template_name='my_app:work-other-page')

    def test_service_model_loads_in_page_template(self, service_type=0, template_name='my_app:service-page'):
        self.make_service(service_type=service_type)
        response = self.client.get(reverse(template_name))
        content = response.content.decode('utf-8')
        response_context_job = response.context['services']

        # Check if post appears in page
        self.assertIn('service_title', content)
        self.assertIn('+32 123 456', content)
        self.assertEqual(len(response_context_job), 1)

    def test_service_domestic_model_loads_in_page(self):
        self.test_service_model_loads_in_page_template(service_type=1, template_name='my_app:service-domestic-page')

    def test_service_healthy_beauty_model_loads_in_page(self):
        self.test_service_model_loads_in_page_template(service_type=2, template_name='my_app:service-healthy-beauty-page')  # noqa: 501E

    def test_service_transport_model_loads_in_page(self):
        self.test_service_model_loads_in_page_template(service_type=3, template_name='my_app:service-transport-page')

    def test_service_food_model_loads_in_page(self):
        self.test_service_model_loads_in_page_template(service_type=4, template_name='my_app:service-food-page')

    def test_service_technic_model_loads_in_page(self):
        self.test_service_model_loads_in_page_template(service_type=7, template_name='my_app:service-technic-page')

    def test_service_other_model_loads_in_page(self):
        self.test_service_model_loads_in_page_template(service_type=20, template_name='my_app:service-other-page')
