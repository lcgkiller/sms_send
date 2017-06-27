from django import forms

class smsForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=12)
