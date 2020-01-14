from django.contrib import admin
from django.urls import re_path

from .views import (
	home,
	login,
	singup,
	)

urlpatterns = [
	re_path(r'^$', home, name = 'home'),
	re_path(r'login', login, name = 'login'),
	re_path(r'singup', singup, name = 'singup'),
]
