from django import forms
from .models import Tovar, Tovar_inphoto


class TovarForm(forms.ModelForm):

    class Meta:
        model = Tovar
        fields = ['tovar_name', 'tovar_slug', 'tovar_info', 'tovar_image', 'tovar_made', 'tovar_price',
                  'tovar_url', 'tovar_stock', 'tovar_available']
