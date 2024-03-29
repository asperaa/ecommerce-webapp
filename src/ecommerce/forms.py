from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class ContactForm(forms.Form):

    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {
                "class": "form-control",
                "placeholder": "Your full name"
             }
        )
    )
    email = forms.CharField(widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your message"
            }
        ))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Your message"
            }
        )
    )

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not '@gmail.com' in email:
    #         raise forms.ValidationError("Email has to be gmail")
    #     return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):


    username = forms.CharField(
        widget=forms.TextInput(
            attrs=
            {
                "class": "form-control",
                "placeholder": "username"
            }
        )
    )

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs=
            {
                "class": "form-control",
                "placeholder": "Password"
            }))

    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs=
            {
                "class": "form-control",
                "placeholder": "Confirm password"
            }))

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)

        if qs.exists:
            raise forms.ValidationError("Username taken")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)

        if qs.exists:
            raise forms.ValidationError("email taken")
        return email

    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2!=password:
            raise forms.ValidationError("Passwords must match!")
        return data