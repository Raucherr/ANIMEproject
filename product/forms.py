from django import forms

from .models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'