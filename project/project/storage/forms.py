from django import forms

from project.storage.models import Storage


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = '__all__'


class ChooseStorageForm(StorageForm):
    class Meta(StorageForm.Meta):
        widgets = {
            'capacity': forms.NumberInput(
                attrs={'placeholder': 'Capacity (GB)'}
            ),
            'read_speed': forms.NumberInput(
                attrs={'placeholder': 'Read speed (MB/s)'}
            ),
            'write_speed': forms.NumberInput(
                attrs={'placeholder': 'Write speed (MB/s)'}
            )
        }
