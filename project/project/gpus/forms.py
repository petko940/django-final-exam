from django import forms

from project.gpus.models import AllGpus


class BaseGpuForm(forms.ModelForm):
    class Meta:
        model = AllGpus
        fields = "__all__"


class ChooseGpuForm(BaseGpuForm):
    class Meta(BaseGpuForm.Meta):
        fields = (
            'manufacturer',
            'name',
            'release_year',
            'memory_size',
            # 'gpu_clock',
            # 'memory_clock',
            # 'memory_type',
        )

