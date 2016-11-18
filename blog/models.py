from django.db import models
from django.utils import timezone
#all objects are called models

# Create your models here.
class Post(models.Model):#defines our Post model (object)
	author = models.ForeignKey('auth.User')#link to another model
	title = models.CharField(max_length=200)#define text with limited number of characters
	text = models.TextField()#long text without limit
	created_date = models.DateTimeField(default= timezone.now)#date and time
	published_date = models.DateTimeField(blank=True, null = True)

	def publish(self):#
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title