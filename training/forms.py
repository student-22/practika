from django import forms


def is_capital(value):
    if value[0] != value[0].title():
        raise forms.ValidationError('first letter must be uppercase')

def valid_age(value):
    if value < 14:
        raise forms.ValidationError('Age must be positive and elder than 14')

def valid_phone_number(value):
    if value[0:4] != '+996' and len(value) != 10:
        raise forms.ValidationError('Phone number must start +996 and contain 10 digits')



class UserForm(forms.Form):
    first_name = forms.CharField(max_length=25, validators=[is_capital])
    last_name = forms.CharField(max_length=25, validators=[is_capital])
    age = forms.IntegerField(validators=[valid_age])
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10, validators=[valid_phone_number])
