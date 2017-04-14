from django import forms
from .models import Tovar, Tovar_inphoto


class TovarForm(forms.ModelForm):

    class Meta:
        model = Tovar
        fields = ['tovar_name', 'tovar_slug', 'tovar_info', 'tovar_image', 'tovar_made', 'tovar_price',
                  'tovar_url', 'tovar_stock', 'tovar_available']


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)