from django import forms
from .models import UserText, UserFile

class TextForm(forms.Form):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'style': 'width: 250px'
                }
            ))
    message = forms.CharField(max_length=3000, widget=forms.Textarea(
                attrs={
                    'class':'form-control',
                    'style':'width: 700px'
                }
            ))
    
    class Meta:
        fields = ['username', 'message']

class FileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'style':'width: 250px',
                }
            ))
    file = forms.FileField(widget=forms.FileInput(
                attrs={
                    'class':'form-control',
                    'style':'width: 200px',
                }
            ))
    class Meta:
        model = UserFile
        fields = ('username', 'file')