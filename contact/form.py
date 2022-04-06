from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.CharField(label='Your Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=200)
    message = forms.Textarea()
