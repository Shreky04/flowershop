import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget
from django.utils import timezone

from .models import Comments, User, Order


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ("publish_date", "author", "item")


class UserProfileCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=False)
    dateofbirth = forms.DateField(required=False, input_formats=['%Y-%m-%d'])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone', 'dateofbirth']


class OrderForm(forms.ModelForm):
    quantity = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], label='Кількість')
    street = forms.CharField(max_length=100, label='Вулиця', required=True)
    house = forms.CharField(max_length=10, label='Дім', required=True)
    apartment = forms.CharField(max_length=10, label='Квартира', required=True)

    class Meta:
        model = Order
        fields = ['quantity', 'street', 'house', 'apartment']
