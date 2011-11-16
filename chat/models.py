from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
	start_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	owner = models.CharField(max_length=30)
	end_date = models.DateTimeField()
	department = models.ForeignKey('Department',null=True,blank=True)
	def __unicode__(self):
		return self.title


class Message(models.Model):
	body = models.TextField()
	date_sent = models.DateTimeField(auto_now=True)
	date_edited = models.DateTimeField(null=True,blank=True)
	ip = models.IPAddressField()
	chat = models.ForeignKey(Chat)
	def __unicode__(self):
		return self.chat.title

class Department(models.Model):
	name = models.CharField(max_length=128)
	users = models.ManyToManyField(User)
	def __unicode__(self):
		return self.name
	