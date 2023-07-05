from django import forms

from project.ram.models import RAM


class RAMForm(forms.ModelForm):
    class Meta:
        model = RAM
        fields = '__all__'
        widgets = {
            'memory_type': forms.Select(attrs={'onchange': 'updateSpeedChoices()'}),
        }


class DeleteRamForm(RAMForm):
    class Meta(RAMForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True