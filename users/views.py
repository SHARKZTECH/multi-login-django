from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ParentSignUpForm,StaffSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User,Parent
# Create your views here.

def register(request):
	
	return render(request,'register.html',{})

class ParentSignUpView(CreateView):
	model=User
	form_class=ParentSignUpForm
	template_name='signup.html'

	def get_content_data(self,**kwargs):
		kwargs['user_type']='parent'
		return super().get_content_data(**kwargs)
	def form_valid(self,form):
		user=form.save()
		login(self.request,user)
		return redirect('home')

class StaffSignUpView(CreateView):
	model=User
	form_class=StaffSignUpForm
	template_name='signup.html'

	def get_content_data(self,**kwargs):
		kwargs['user_type']='staff'
		return super().get_content_data(**kwargs)
	def form_valid(self,form):
		user=form.save()
		login(self.request,user)
		return redirect('home')





# @login_required
# def profile(request):
# 	if request.method=="POST":
# 		u_form=UserUpdateForm(request.POST,instance=request.user)
# 		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
# 		if u_form.is_valid() and p_form.is_valid():
# 			u_form.save()
# 			p_form.save()
# 			messages.success(request,"Profile has been updated successfully!")
# 			return redirect('user_profile')
# 	else:
# 		u_form=UserUpdateForm(instance=request.user)
# 		p_form=ProfileUpdateForm(instance=request.user.profile)
# 	context={
# 	'u_form':u_form,
# 	'p_form':p_form
# 	}
# 	return render(request,'profile.html',context)

