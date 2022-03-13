from dataclasses import field
from xml.dom.minidom import Attr
from django import forms

from common.models import Customer



class CustomerRegForm(forms.ModelForm):
    genter=(('m','male'),('f','female'),)


    cust_name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Name',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # cust_email = forms.CharField(label='Name',widget=forms.RadioSelect(attrs={'class':'form-control'}))
    cust_email = forms.CharField(label='Name',widget=forms.Select(choices=genter))
    class Meta:
        
        model= Customer
        fields=('cust_name','email_id','phone_no','password')
        # field='__all__'
        # exclude=('cust_id',)