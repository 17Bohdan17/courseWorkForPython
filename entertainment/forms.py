from .models import EntertainmentCenter, CenterType, Visitor, Event
from django import forms


# Форма для створення або редагування розважального центру
class EntertainmentCenterForm(forms.ModelForm):
    class Meta:
        model = EntertainmentCenter
        fields = ['name', 'description', 'address', 'center_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'center_type': forms.Select(attrs={'class': 'form-select'}),
        }


# Форма для створення або редагування типу центру
class CenterTypeForm(forms.ModelForm):
    class Meta:
        model = CenterType
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


# Форма для створення або редагування відвідувача

# forms.py
class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['username', 'email']



    # Використовуємо конструктор для того, щоб список центрів був динамічним
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['center_id'].queryset = EntertainmentCenter.objects.all()  # Список доступних центрів

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'entertainment_center', 'description']
