from django import forms
from .models import WorkModel
from django.forms import ModelForm


class WorkForm(ModelForm):

    class Meta:
        model = WorkModel
        fields = '__all__'

        PROFESSION_CHOICES = (
            ('Carreleur/Ladrilhador Azulejador', 'Carreleur/Ladrilhador Azulejador'),
            ('Charpentier/Carpinteiro', 'Charpentier/Carpinteiro'),
            ('Coffreur/Cofragem', 'Coffreur/Cofragem'),
            ('Couvreur/Carpinteiro(telhado)', 'Couvreur/Carpinteiro(telhado)'),
            ('Ferrailleur/Armador de Ferro', 'Ferrailleur/Armador de Ferro'),
            ('Chauffage/Aquecimento', 'Chauffage/Aquecimento'),
            ('Maçon/Pedreiro', 'Maçon/Pedreiro'),
            ('Plombier/Encanador', 'Plombier/Encanador'),
            ('Peintre/Pintor', 'Peintre/Pintor'),
            ('Plafonneur', 'Plafonneur'),
            ('Masticage', 'Masticage'),
            ('Ajudante', 'Ajudante')
        )
        LANGUAGE_CHOICES = (('Frances', 'Frances'), ('Ingles', 'Ingles'), ('Neerlandes', 'Neerlandes'))

        widgets = {
            'profession': forms.Select(choices=PROFESSION_CHOICES, attrs={'class': 'form-control'}),
            'language': forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'form-control'})
        }

        error_messages = {
            
        }











