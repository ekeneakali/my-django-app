from django import forms

from.models import *

from django.core import validators

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)



class Register(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'enter your email'}))
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter password2'}))
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image', 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.image = self.cleaned_data['image']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user

class AddPost(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])



    class Meta():
        model = Post
        fields = '__all__'

class AddContact(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Contact
        fields = '__all__'

class AdvertisementForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Advertisement
        fields = '__all__'

class EditProfile(UserChangeForm):

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class PasswordForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Password
        fields = '__all__'

class VideoForm(forms.ModelForm):
    botfield = forms. CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


    class Meta():
        model = Video
        fields = '__all__'


        







