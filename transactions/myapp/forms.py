from django import forms

class MoneyhubForm(forms.Form):
    client_id = forms.CharField(label='Client ID', required=True)
    secret_key = forms.CharField(label='Secret Key', required=True)
