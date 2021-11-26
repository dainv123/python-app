from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Beast, Book

class SignUpForm(UserCreationForm):
  birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

  class Meta:
    model = User
    fields = ('username', 'birth_date', 'password1', 'password2')

class BeastForm(ModelForm):
    class Meta: 
        model = Beast
        fields = '__all__'

class BookForm(ModelForm):
  class Meta:
    model = Book
    fields = '__all__'
