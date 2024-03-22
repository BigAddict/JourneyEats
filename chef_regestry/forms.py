from django import forms
from .models import Chef

class ChefForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user

    class Meta:
        model = Chef
        exclude = ['user']
        widgets = {
            'bio': forms.TextInput(attrs={'class':"form-control col-sm-10"})
        }