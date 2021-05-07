from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from prime.models import CouponCode
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', max_length=50, help_text=None, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',max_length=50, help_text=None, widget=forms.PasswordInput())
    referer = forms.CharField(label='referer', required=False, max_length=50,widget=forms.TextInput(attrs={'placeholder':'optional'}))
    class Meta:
        model = Account
        fields = ('fullname','email','username','password1','password2','coupon','referer')

    def clean(self):
        coupon = self.cleaned_data['coupon']
        try:
            code = CouponCode.objects.get(code=coupon, valid=True)
        except CouponCode.DoesNotExist:
            raise forms.ValidationError('invalid coupon code ')

        if Account.objects.filter(coupon=code).exists():
            raise forms.ValidationError('this coupon already exist')
        if code.active==False:
            raise forms.ValidationError('the coupon has expired') 
    

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    class Meta:
        model = Account
        fields = ('email','password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('invalid credentials entered by user')

    