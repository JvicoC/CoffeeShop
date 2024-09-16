from django import forms
from .models import Product

class ProductForm(forms.Form):
    name= forms.CharField(max_length=200, label="nombre")
    description = forms.CharField(max_length=300, label="descripcion")
    price=forms.DecimalField(max_digits=10, decimal_places=2, label="precio", initial=20.00)
    available=forms.BooleanField(initial=True,label="disponible", required=False)
    photo= forms.ImageField(label="foto",required=False)
    #otro=forms.DateField()

    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
        )

class ProductFormEdit(forms.Form):
    id= forms.CharField(max_length=200, label="ID", initial=Product.objects.filter(id=3).first().id)
    name= forms.CharField(max_length=200, label="nombre", initial=Product.objects.filter(id=3).first().name)
    description = forms.CharField(max_length=300, label="descripcion",initial=Product.objects.filter(id=3).first().description)
    price=forms.DecimalField(max_digits=10, decimal_places=2, label="precio", initial=Product.objects.filter(id=3).first().price)
    available=forms.BooleanField(initial=Product.objects.filter(id=3).first().available,label="disponible", required=False)
    photo= forms.ImageField(label="foto",required=False)

    def update(self, idupdate):
        Product.objects.filter(id=idupdate).update(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
        )