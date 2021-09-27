from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User,Parent,Staff
from django.db import transaction



class ParentSignUpForm(UserCreationForm):
	email=forms.EmailField(required=True)
	fullnames=forms.CharField(max_length=100)
	telephone=forms.IntegerField()
	country=forms.CharField(max_length=100)
	city=forms.CharField(max_length=100)
	address=forms.CharField(max_length=100)

	class Meta:
		model=User
		fields=['username','fullnames','email','telephone','country','city','address']
	@transaction.atomic
	def save(self, *args, **kwargs):
		user=super().save(commit=False)
		user.email=self.cleaned_data.get('email')
		user.is_parent=True
		user.save()
		parent=Parent.objects.create(user=user)
		parent.fullnames=self.cleaned_data.get('fullnames')
		parent.telephone=self.cleaned_data.get('telephone')
		parent.country=self.cleaned_data.get('country')
		parent.city=self.cleaned_data.get('city')
		parent.address=self.cleaned_data.get('address')

		parent.save()
		return user 

class StaffSignUpForm(UserCreationForm):
	email=forms.EmailField(required=True)
	fullnames=forms.CharField(max_length=100)
	telephone=forms.IntegerField()
	city=forms.CharField(max_length=100)
	address=forms.CharField(max_length=100)
	nationid=forms.IntegerField()


	class Meta:
		model=User
		fields=['username','fullnames','email','telephone','nationid','city','address']
	@transaction.atomic
	def save(self, *args, **kwargs):
		user=super().save(commit=False)
		user.email=self.cleaned_data.get('email')
		user.is_staff=True
		user.save()
		staff=Staff.objects.create(user=user)
		staff.fullnames=self.cleaned_data.get('fullnames')
		staff.telephone=self.cleaned_data.get('telephone')
		staff.city=self.cleaned_data.get('city')
		staff.address=self.cleaned_data.get('address')
		staff.nationid=self.cleaned_data.get('nationid')
		staff.save()
		return user 


# class UserUpdateForm(forms.ModelForm):
# 	email=forms.EmailField()
# 	# telephone=forms.IntegerField()
# 	# country=forms.CharField(max_length=100)
# 	# city=forms.CharField(max_length=100)
# 	# address=forms.CharField(max_length=100)

# 	class Meta:
# 		model=User
# 		fields=['username','email']


# class ProfileUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model=Profile
# 		fields=['image']
