from django import forms
from .models import Customer,CartItem
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User   # iske through user badha rhe h




class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput({'class':'abc'}))
    password2=forms.CharField(widget=forms.PasswordInput({'class':'abc'}))
    class Meta:   #database se field le rhe h isiye Meta krte h
        model=User
        fields=['username','first_name','last_name','email']#kitni field chahiye ye uske liye all kro ya perticular name  specify kro
             
        widgets={
            'username':forms.TextInput(attrs={'class':'abc',
                                              'placeholder':'random'}),
            'first_name':forms.TextInput(attrs={'class':'abc'}),
            'last_name':forms.TextInput(attrs={'class':'abc'}),
            'email':forms.TextInput(attrs={'class':'abc'}),

             }
        
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(max_length=40,label=('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
#------------------------------------------------
# Customer Profile show

class CustomerProfileView(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class CartItemForm(forms.ModelForm):
    class Meta:
        model=CartItem
        fields='__all__'
    
        
        