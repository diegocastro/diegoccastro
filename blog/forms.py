from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        form = self.cleaned_data
        body = render_to_string('blog/contact/email.html', {'form': form})

        email = EmailMessage('Contato site', body, 'diego@diegoccastro.com', ['castroc.diego@gmail.com'])
        email.content_subtype = 'html'
        email.send()
