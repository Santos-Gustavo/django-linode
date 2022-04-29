from django import forms
from .models import WorkModel
from django.forms import ModelForm


class WorkForm(ModelForm):
    class Meta:
        model = WorkModel
        fields = '__all__'
        # exclude = 'date'
        # widget = {
        #     'name': forms.Textarea(attrs={'class': 'myform', 'placeholder': 'Entre teu nome'})
        # }

        # ############################# CHOICES ############################# #
        # PROFESSION_CHOICES = (
        # (1, 'Carreleur/Ladrilhador Azulejador'),
        # (2, 'Charpentier/Carpinteiro'),
        # (3, 'Coffreur/Cofragem'),
        # (4, 'Couvreur/Carpinteiro(telhado)'),
        # (5, 'Ferrailleur/Armador de Ferro'),
        # (6, 'Chauffage/Aquecimento'),
        # (7, 'Maçon/Pedreiro'),
        # (8, 'Plombier/Encanador'),
        # (9, 'Peintre/Pintor'),
        # (10, 'Plafonneur'),
        # (11, 'Masticage'),
        # (12, 'Ajudante')
        # )

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











