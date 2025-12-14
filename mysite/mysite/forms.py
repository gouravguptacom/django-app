from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label="value 1", required=False, widget=forms.Textarea(attrs={'class': 'active'}))
    num2=forms.CharField(label="value 2", widget=forms.Textarea(attrs={'class': 'active'}))
    email=forms.EmailField()