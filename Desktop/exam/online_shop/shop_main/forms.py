from django import forms
from shop_main.models import Product, Comments


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'new_price', 'description']


# Comments form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'body']
