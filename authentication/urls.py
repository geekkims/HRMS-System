from django.urls import include, path
from . import views

urlpatterns = [
   path('signup/',views.signup, name="signup"),
   path('signin/',views.signin, name="signin"),
   path('signout/',views.signout, name="signout"),
    path('resetpassword/',views.resetpassword, name="resetpassword"),
]
