from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, NumberInput
from .models import Expectation


class ExpectationForm(ModelForm):
    name = CharField(widget=TextInput(
        attrs={
            'placeholder': 'What is your name?',
            'class': 'name',
        })
    )
    email = EmailField(widget=EmailInput(
        attrs={'placeholder': "Your email address",
               'class': 'email',
               })
    )
    phone_number = CharField(widget=NumberInput(
        attrs={'placeholder': "Your your phone number",
               'class': 'phone',
               })
    )
    # Metadata
    class Meta:
        model = Expectation
        fields = ('name', 'email', "phone_number", "what_you_say")
