
   
from django import forms
from .models import   siteModel
from django.forms import TextInput




class siteForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         kwargs.setdefault('label_suffix', '')
         super(siteForm, self).__init__(*args, **kwargs)
         self.fields['url'].widget.attrs.update({'id':'textInput','class': '"appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"','placeholder':'Enter the URL'})
    
     class Meta:
        model = siteModel
        labels = {
            'url': '',
            
        }
        fields = ['url']
       
#class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-password"
    
        