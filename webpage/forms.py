from dataclasses import fields
from pyexpat import model
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm
from .models import Position, Projects

class requestForm(forms.Form):
   name = forms.CharField(max_length = 100)
   email = forms.CharField(widget = forms.EmailInput())
   date = forms.DateField(widget = forms.DateInput())
   time = forms.TimeField(widget = forms.TimeInput())
   message = forms.CharField(max_length = 100)

class Projectform(ModelForm):
   class Meta:
      model = Projects
      fields = '__all__'

class PositionForm(ModelForm):
   class Meta:
      model = Position
      fields = '__all__'