from django.shortcuts import render
from django.utils import timezone
from .models import Post#need to include model from models.py 
#.(name of file without.py) is possible since views.py and models.py are in same directory

#we want to take models saved in db and display it in template. We do this using views.py

# Create your views here.
def post_list(request):#request : everything we receive from user via internet
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})#blog/post_list.html is the template file