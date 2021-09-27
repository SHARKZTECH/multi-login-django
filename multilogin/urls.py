"""multilogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *
from users.views import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),

    path('register/',register,name='register_user'),
    path('users/register/parent',ParentSignUpView.as_view(),name='parent_signup'),
    path('users/register/staff',StaffSignUpView.as_view(),name='staff_signup'),

    # path('profile/',profile,name='user_profile'),
      path('login/',LoginView.as_view(template_name='login.html'),name='login_user'),
     path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout_user'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)