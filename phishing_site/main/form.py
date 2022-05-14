
   
from django import forms
from .models import   siteModel
from django.forms import TextInput




class siteForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(siteForm, self).__init__(*args, **kwargs)
    
     class Meta:
        model = siteModel
        labels = {
            'url': 'Enter the URL',
            
        }
        fields = ['url']
       
        widgets = {
            'id':'textInput',
            
        }
        