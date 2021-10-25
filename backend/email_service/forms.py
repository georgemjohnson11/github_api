from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    contactName = forms.CharField(label='contactName', max_length=100)
    contactSubject = forms.CharField(label='contactSubject', widget=forms.Textarea)
    contactSenderEmail = forms.EmailField(label='contactSenderEmail')
    authorization = forms.BooleanField(label='authorization', required=True)
    contactMessage = forms.CharField(label='contactMessage', widget=forms.Textarea, max_length=400)