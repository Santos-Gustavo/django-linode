from django import forms
from .models import WorkModel, ServiceModel
from django.forms import ModelForm

error_messages_work = {'salary': {'max_value': 'Valor máximo por hora é de €99.99'}}


class WorkConstructionForm(ModelForm):
    # ToDo: Set values in _CHOICES to int, it will improve for DataBase, eg: "
    #  (1, 'Plafonneur'),
    #  (2, 'Masticage'),
    #  (3, 'Ajudante')"
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
        TYPEJOB_CHOICES = ((1, 'Construção'),)

        widgets = {
            'profession': forms.Select(choices=PROFESSION_CHOICES, attrs={'class': 'form-control'}),
            'language': forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'form-control'}),
            'type_job': forms.Select(choices=TYPEJOB_CHOICES, attrs={'class': 'form-control'})
        }

        error_messages = error_messages_work


class WorkCleaningForm(ModelForm):
    class Meta:
        model = WorkModel
        fields = '__all__'

        PROFESSION_CHOICES = (
            ('Nettoyage de bureau/Limpeza de escritório', 'Nettoyage de bureau/Limpeza de escritório'),
            ('Nettoyage de maison/Limpeza residencial', 'Nettoyage de maison/Limpeza residencial'),
            ('Nettoyage chantier/Limpeza pós-obra', 'Nettoyage chantier/Limpeza pós-obra'),
        )
        LANGUAGE_CHOICES = (('Frances', 'Frances'), ('Ingles', 'Ingles'), ('Neerlandes', 'Neerlandes'))
        TYPEJOB_CHOICES = ((2, 'Limpeza'),)

        widgets = {
            'profession': forms.Select(choices=PROFESSION_CHOICES, attrs={'class': 'form-control'}),
            'language': forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'form-control'}),
            'type_job': forms.Select(choices=TYPEJOB_CHOICES, attrs={'class': 'form-control'})
        }
        error_messages = error_messages_work


class WorkOtherForm(ModelForm):
    class Meta:
        model = WorkModel
        fields = '__all__'

        LANGUAGE_CHOICES = (('Frances', 'Frances'), ('Ingles', 'Ingles'), ('Neerlandes', 'Neerlandes'))
        TYPEJOB_CHOICES = ((3, 'Outro'),)

        widgets = {
            'language': forms.Select(choices=LANGUAGE_CHOICES, attrs={'class': 'form-control'}),
            'type_job': forms.Select(choices=TYPEJOB_CHOICES, attrs={'class': 'form-control'})
        }
        error_messages = error_messages_work


class ServiceForm(ModelForm):
    class Meta:
        model = ServiceModel
        fields = '__all__'
        TYPESERVICE_CHOICES = ((1, 'Doméstico'), (2, 'Saúde e Beleza'), (3, 'Transporte'), (4, 'Comida'), (5, 'Aulas'),
                               (6, 'Viagens'), (7, 'Técnico'), (20, 'Outros'))
        widgets = {
            'type_service': forms.Select(choices=TYPESERVICE_CHOICES, attrs={'class': 'form-control'})
        }
