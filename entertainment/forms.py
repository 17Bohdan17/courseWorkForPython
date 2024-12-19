from .models import EntertainmentCenter, CenterType, Visitor, Event
from django import forms

# Форма для створення/редагування розважального центру
class EntertainmentCenterForm(forms.ModelForm):
    class Meta:
        model = EntertainmentCenter
        fields = ['name', 'description', 'address', 'center_type']  # Поля форми
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Поле назви з класом для стилю Bootstrap
            'description': forms.Textarea(attrs={'class': 'form-control'}),  # Текстове поле для опису
            'address': forms.TextInput(attrs={'class': 'form-control'}),  # Поле для введення адреси
            'center_type': forms.Select(attrs={'class': 'form-select'}),  # Випадаючий список типів центру
        }

# Форма для створення/редагування типу розважального центру
class CenterTypeForm(forms.ModelForm):
    class Meta:
        model = CenterType
        fields = ['name', 'description']  # Поля форми
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Поле назви
            'description': forms.Textarea(attrs={'class': 'form-control'}),  # Поле для опису
        }

# Форма для створення/редагування відвідувача
class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['username', 'email']  # Поля форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Динамічне заповнення списку центрів при створенні відвідувача
        self.fields['center_id'].queryset = EntertainmentCenter.objects.all()

# Форма для створення/редагування події
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'entertainment_center', 'description']  # Поля форми
