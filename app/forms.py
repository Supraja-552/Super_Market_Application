from app.models import *
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields='__all__'
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'