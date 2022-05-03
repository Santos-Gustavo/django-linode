from django.urls import path
from .views import *

app_name = 'my_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('success/', SuccessView.as_view(), name='success-page'),
    path('work/', WorkView.as_view(), name='work-page'),
    path('work/form/', WorkCreateView.as_view(), name='work-form-page'),
    path('work/construction/', Construction.as_view(), name='work-construction'),
    # path('work/construction/', views.WorkView.cleaning, name='work-cleaning'),
]
