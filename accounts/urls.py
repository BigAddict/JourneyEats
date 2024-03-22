from django.urls import path
from .views import registration, signin, signout, ProfileTemplateView

urlpatterns = [
    path("", signin, name="signin"),
	path('register/', registration, name ="register"),
    path("signout/", signout, name="signout"),
    path("profile/", ProfileTemplateView.as_view(), name="profile")
]
