from django.contrib.auth.models import User
from django import forms
from .models import register_model
from django.contrib.auth.forms import UserCreationForm
import hashlib


#class UserForm(forms.ModelForm):
class SignupForm(forms.ModelForm):
    #username = forms.CharField(max_length=200, help_text='Required')
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta: #information about a class
        model = register_model
#ek tarike se ye hua kii user naam kii table already hai admin mai toh yaha entities nii deni hongi beacuase by default humne aise define kr diya user ko blue print mai (model)

        fields = ['firstname', 'lastname', 'username' , 'email', 'password']


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_passsword")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    # def make_password(self):
    #     password = self.cleaned_data.get("password")
    #     hash = hashlib.md5(password).hexdigest()
    #     return hash

    '''def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    '''

    '''def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
'''
