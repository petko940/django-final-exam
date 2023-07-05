from django import forms

from project.cpus.models import AllCpus, ChosenCpus, CustomCpu


class BaseCpuForm(forms.ModelForm):
    class Meta:
        model = AllCpus
        fields = "__all__"


class ChooseCpuForm(BaseCpuForm):
    pass


class ChooseCpuListForm(BaseCpuForm):
    class Meta(BaseCpuForm.Meta):
        fields = (
            'brand',
            'name',
            'cores',
            'threads',
            # 'base_frequency',
            # 'max_turbo_frequency',
            # 'tdp'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label_suffix = ''


class CustomCpuForm(forms.ModelForm):
    class Meta:
        model = CustomCpu
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'CPU Name'}),
            'manufacturer': forms.TextInput(attrs={'placeholder': 'Manufacturer'}),
            'clock_speed': forms.NumberInput(attrs={'placeholder': 'Clock speed (GHz)'}),
            'number_of_cores': forms.NumberInput(attrs={'placeholder': 'Number of cores'}),
            'cache_size': forms.NumberInput(attrs={'placeholder': 'Cache (MB)'}),
        }
        labels = {
            'max_ram': 'Max RAM',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label_suffix = ''


class DeleteCpuForm(BaseCpuForm):
    class Meta(CustomCpuForm.Meta):
        model = ChosenCpus
        fields = '__all__'
