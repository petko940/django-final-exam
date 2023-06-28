from django import forms

from project.cpus.models import AllCpus


class BaseCpuForm(forms.ModelForm):
    class Meta:
        model = AllCpus
        fields = "__all__"


class ChooseCpuForm(BaseCpuForm):
    pass


class ChooseCpuListForm(BaseCpuForm):
    class Meta:
        model = AllCpus
        fields = (
            'brand',
            'name',
            'cores',
            'threads',
            'max_turbo_frequency',
            'base_frequency',
            'tdp'
        )

