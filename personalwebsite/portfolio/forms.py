from datetime import datetime

from django import forms
from django.core.mail import send_mail

from .models import Contact, Spam


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    )
    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'style': 'height: 10em;'}),
    )
    website = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'style': 'display: none;'}),
    )

    def honeypot_empty(self):
        return len(self.cleaned_data['website']) == 0

    def save_contact(self, ip, user_agent):
        contact = Contact(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message'],
            ip_address=ip,
            user_agent=user_agent,
        )
        contact.save()

    def save_spam(self, ip, user_agent):
        spam = Spam(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message'],
            website=self.cleaned_data['website'],
            ip_address=ip,
            user_agent=user_agent,
        )
        spam.save()

    def send_email(self):
        message = 'Name: ' + self.cleaned_data['name'] + \
            '\nEmail: ' + self.cleaned_data['email'] + \
            '\nSubject: ' + self.cleaned_data['subject'] + \
            '\n\n' + self.cleaned_data['message']

        send_mail(
            'Personal Website Contact: ' + self.cleaned_data['subject'],
            message,
            'lee@leemccarthy.com',
            ['lee@leemccarthy.com'],
        )
