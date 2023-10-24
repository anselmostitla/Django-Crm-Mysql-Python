from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
  email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
  first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}))
  last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))
  
  class Meta():
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, *kwargs)
    
    # self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['class'] = 'flex flex-col border-2 w-[100%] px-2 py-2 outline-none my-2 rounded'
    self.fields['username'].widget.attrs['placeholder'] = 'Username'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    self.fields['first_name'].widget.attrs['class'] = 'flex flex-col border-2 w-[100%] px-2 py-2 outline-none my-2 rounded'
    self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
    self.fields['last_name'].widget.attrs['class'] = 'flex flex-col border-2 w-[100%] px-2 py-2 outline-none my-2 rounded'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
    self.fields['email'].widget.attrs['class'] = 'flex flex-col border-2 w-[100%] px-2 py-2 outline-none my-2 rounded'
    self.fields['email'].widget.attrs['placeholder'] = 'Email Address'

    # self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'flex flex-col border-2 w-[100%] p-2 outline-none rounded'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<ul class="text-xs"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

    self.fields['password2'].widget.attrs['class'] = 'flex flex-col border w-[100%] px-2 py-2 outline-none rounded'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

# Create add record form
class AddRecordForm(forms.ModelForm):
  first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class':'border p-2 rounded outline-none w-full my-1'}), label="")
  last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Zipcode', 'class':'border p-2 rounded outline-none w-full my-1'}), label="") 
  
  class Meta:
    model = Record
    exclude = ("user", )
  