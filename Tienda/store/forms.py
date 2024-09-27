from django import forms
from .import models

class CreateProducts(forms.ModelForm):
    class Meta:
        model=models.gafas
        fields=['ItemName','ItemCategory','Price']

class bodega(forms.ModelForm):
    class Meta:
        model=models.bodega
        fields=['BodegaID','location','ItemStock']

