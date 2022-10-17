from django import forms
from models.models import URL, IMAGE, NOTE

class URLForm(forms.ModelForm):
    
    class Meta:
        model = URL
        fields = '__all__'
        widgets = { 'mark' : forms.Select(
            attrs= {
                'visible': 'false'
            },
            ), 
        }

class IMAGEForm(forms.ModelForm):
    
    class Meta:
        model = IMAGE
        fields = '__all__'

class NOTEForm(forms.ModelForm):
    
    class Meta:
        model = NOTE
        fields = '__all__'


