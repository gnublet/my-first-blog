from django.conf.urls import url
from . import views

#use this to keep /mysite/urls.py urlpatterns clean.
urlpatterns=[
	url(r'^$', views.post_list, name='post_list'),
]