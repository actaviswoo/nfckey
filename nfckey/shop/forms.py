"""
Формы для приложения shop.
"""
from django import forms
from .models import Order, Product


class OrderForm(forms.ModelForm):
    """
    Форма для создания заказа.
    """
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'phone', 'custom_text', 'quantity']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 123-45-67'
            }),
            'custom_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Введите текст для гравировки на брелоке'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'value': 1
            }),
        }
        labels = {
            'customer_name': 'Имя',
            'email': 'Email',
            'phone': 'Телефон',
            'custom_text': 'Текст для гравировки',
            'quantity': 'Количество',
        }

