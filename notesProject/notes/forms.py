# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'password1', 'password2']

# 	def __init__(self, *args, **kwargs):
# 		super(CustomUserCreationForm, self).__init__(self, *args, **kwargs)
# 		self.fields['username'].widget.attrs.update({'class': 'contact_form_item', 'placeholder' : 'Username'})
# 		self.fields['password1'].widget.attrs.update({'class': 'contact_form_item', 'placeholder' : 'Password'})
# 		self.fields['password2'].widget.attrs.update({'class': 'contact_form_item', 'placeholder' : 'Confirm password'})