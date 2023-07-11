from django import forms
from django.forms import ModelForm
from project.common.models import ShowPC
from project.cpus.models import ChosenCpus, AllCpus


# class ShowPCForm(ModelForm):
#     class Meta:
#         model = ShowPC
#         fields = '__all__'


class ShowPCForm(ModelForm):
    class Meta:
        model = ShowPC
        fields = '__all__'
