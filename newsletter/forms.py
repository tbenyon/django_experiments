from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if len(email.split('@')) != 2:
            raise forms.ValidationError('You should have one "@" in your address.')

        base, hostname = email.split('@')
        if hostname != "ths.uk.net":
            raise forms.ValidationError('Please ensure you use a "ths.uk.net" e-mail address.')

        return email