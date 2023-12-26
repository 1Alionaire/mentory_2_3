from products.models import Product, ProductCategory
from django import forms

class InputProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), widget=forms.Select())
    price = forms.DecimalField(widget=forms.NumberInput())
    quantity = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'quantity')