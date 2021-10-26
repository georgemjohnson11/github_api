from django import forms
from django.core.mail import send_mail

class RepoForm(forms.Form):
    repo = forms.CharField(label='Repository', max_length=100)
    owner = forms.CharField(label='Owner', max_length=100)

class ContactForm(forms.Form):
    contactName = forms.CharField(label='contactName', max_length=100)
    contactSubject = forms.CharField(label='contactSubject', widget=forms.Textarea)
    contactEmail = forms.EmailField(label='contactEmail')
    authorization = forms.BooleanField(label='authorization', required=True)
    contactMessage = forms.CharField(label='contactMessage', widget=forms.Textarea, max_length=400)