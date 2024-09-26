from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import gafas

class ProductForm(forms.ModelForm):
    class Meta:
        model = gafas
        fields = ['Nombre Item', 'Categoria Item','Precio']

#handles new product creation
def newProduct(View):
    def get(self,request):
        pass
    def post(self,request):
        pass

def viewProduct(view):
    def get(self,request):
        pass

    

