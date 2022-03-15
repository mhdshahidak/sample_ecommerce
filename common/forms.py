from dataclasses import field
from xml.dom.minidom import Attr
from django import forms

from common.models import Customer


class CustomerRegForm(forms.ModelForm):
    # genter=(('m','male'),('f','female'),)

    cust_name = forms.CharField(
        label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_id = forms.CharField(
        label='email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_no = forms.CharField(
        label='phone no', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:

        model = Customer
        fields = ('cust_name', 'email_id', 'phone_no',
                  'password')    # select required field
        # field='__all__'  # select all field
        # exclude=('cust_id',) #select all field excluding cust_id

    def clean_password(self):
        psw = self.cleaned_data['password']

        if len(psw) < 8:
            raise forms.ValidationError(
                'password should be minimum 8 characters')
        return psw
