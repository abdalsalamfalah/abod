from django import forms
class inforeg(forms.Form):
    Full_name=forms.CharField(required=True,widget=forms.TextInput())
    The_age=forms.CharField(required=True,widget=forms.TextInput())
    Phone_num=forms.CharField(required=True,widget=forms.TextInput())
    
