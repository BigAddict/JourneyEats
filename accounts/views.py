from django.db import utils
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpRequest
from typing import Any
from datetime import datetime

from .permissions import create_chef_permissions, create_client_permissions
from .models import Profile

user = get_user_model()

def registration(request:HttpRequest):

	if request.method == "POST":
		email = request.POST['email']
		fname = request.POST['fname']
		lname = request.POST['lname']
		pnumber = "254" + request.POST['pnumber']
		password = request.POST['password']
		user_type = request.POST['user_type']
		try:
			print(request.POST)
			my_user = user.objects.create_user(
				email,
				password,
				first_name = fname,	
				last_name = lname,
				phone_number = pnumber,
				user_type = user_type)
			my_user.save()
			messages.success(request, f"Welcome to JourneyEats {fname}. Please login to continue!")
			return redirect("signin")
		except utils.IntegrityError:
			messages.warning(request, f"{email} is already used. Please login to your account!")
			return redirect("signin")
		except Exception as e:
			messages.warning(request, f"The following error occured.\n{e}.\nPlease contact website admin")
			print(e)
			return redirect("register")
	
	return render(request, "accounts/register.html")

def signin(request:HttpRequest):

	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		my_user = authenticate(request, username=email, password=password)

		if my_user is not None:
			login(request, my_user)
			next_url = request.GET.get('next')
			if next_url:
				messages.success(request, "You're successfully logged in!!Redirecting")
				return redirect(next_url)
			else:
				messages.success(request, "You're successfully logged in!!")
				return redirect("dashboard")
		else:
			messages.warning(request, "Bad credentials!!")
			return redirect("signin")
	return render(request, "accounts/login.html")
	
def signout(request):
	logout(request)
	messages.success(request, "You have successfully logged out!!")
	return redirect("signin")

@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):

	template_name = "accounts/profile.html"

	def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
		self.user = request.user
		return super().get(request, *args, **kwargs)

	def post(self, request:HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
		profile, created = Profile.objects.get_or_create(user = request.user)
		post_data = request.POST

		# Handle profile data
		if request.FILES['profile_picture']:
			profile.profile_picture = request.FILES['profile_picture']
		if post_data['about']:
			profile.about = post_data['about']
		if post_data['gender']:
			profile.gender = post_data['gender']
		if post_data['date_of_birth']:
			profile.date_of_birth = datetime.strptime(post_data['date_of_birth'], '%Y-%m-%d').date()
		if post_data['country']:
			profile.country = post_data['country']
		if post_data['nationality']:
			profile.nationality = post_data['nationality']
		if post_data['state']:
			profile.state = post_data['state']
		if post_data['city']:
			profile.city = post_data['city']
		if post_data['postal_code']:
			profile.postal_code = post_data['postal_code']
		if post_data['language']:
			profile.language = post_data['language']
		if post_data['currency']:
			profile.currency = post_data['currency']
		if post_data['hobbies']:
			profile.hobbies = post_data['hobbies']
		if post_data['interests']:
			profile.interest = post_data['interests']
		if post_data['favourite_activities']:
			profile.favourite_activities = post_data['favourite_activities']
		if post_data['twitter']:
			profile.twitter = post_data['twitter']
		if post_data['facebook']:
			profile.facebook = post_data['facebook']
		if post_data['instagram']:
			profile.instagram = post_data['instagram']
		if post_data['linkedin']:
			profile.linkedin = post_data['linkedin']

		if ['current_password', 'new_password', 'renew_password'] in post_data:
			current_password = post_data['current_password']
			new_password = post_data['new_password']
			renew_password = post_data['renew_password']
			if new_password == renew_password:
				user = authenticate(username=request.user.email, password=current_password)
				if user is not None:
					user.set_password(new_password)
					user.save()
					update_session_auth_hash(request, user)
					messages.success(request, 'Your password has been successfully changed.')
				else:
					messages.error(request, 'Current password is incorrect.')
			else:
				messages.error(request, 'New password and confirmation password do not match.')
		profile.save()
		return super().get(request, *args, **kwargs)