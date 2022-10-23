from django.forms import ModelForm

from general.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['date_created', 'date_modified']

