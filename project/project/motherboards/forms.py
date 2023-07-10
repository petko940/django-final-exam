from django import forms

from project.motherboards.models import Motherboard


class BaseMotherboardForm(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'


class CreateMotherboardForm(BaseMotherboardForm):
    class Meta(BaseMotherboardForm.Meta):
        widgets = {
            'model': forms.TextInput(
                attrs={'placeholder': 'E.g. HD3 B560'}
            ),
            'chipset': forms.TextInput(
                attrs={'placeholder': 'E.g. Intel B560, AMD B450'}
            ),
            'socket': forms.TextInput(
                attrs={'placeholder': 'E.g. LGA1151, AM4'}
            ),
        }
