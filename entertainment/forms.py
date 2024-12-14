from django import forms
from .models import EntertainmentCenter
from .models import CenterType

class EntertainmentCenterForm(forms.ModelForm):
    class Meta:
        model = EntertainmentCenter
        fields = ['name', 'description', 'address', 'center_type']

class CenterTypeForm(forms.ModelForm):
    class Meta:
        model = CenterType
        fields = ['name', 'description']

