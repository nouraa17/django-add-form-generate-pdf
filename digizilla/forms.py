# digizilla/forms.py
from django import forms
from .models import Digizilla

class DigizillaForm(forms.ModelForm):
    class Meta:
        model = Digizilla
        fields = '__all__'
