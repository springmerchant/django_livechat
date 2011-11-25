from django.db import models
from django.contrib.auth.models import User


CHAT_STATUS = (
        ('c', 'Closed'),
        ('t', 'Timed Out'),
		('u', 'Unanswered'),
		('a', 'Active')
    )
class Chat(models.Model):
	start_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	operator = models.ForeignKey('Operator',null=True,blank=True)
	end_date = models.DateTimeField(null=True,blank=True)
	department = models.ForeignKey('Department',null=True,blank=True)
	visitor = models.ForeignKey('Visitor',null=True,blank=True)
	status = models.CharField(max_length=2, choices=CHAT_STATUS)
	
	def __unicode__(self):
		return self.title

class Message(models.Model):
	body = models.TextField()
	date_sent = models.DateTimeField(auto_now=True)
	date_edited = models.DateTimeField(null=True,blank=True)
	ip = models.IPAddressField()
	chat = models.ForeignKey(Chat)
	message_from = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.chat.title

class Department(models.Model):
	name = models.CharField(max_length=128)
	operators = models.ManyToManyField('Operator')
	
	def __unicode__(self):
		return self.name



class Visitor(models.Model):
	user = models.ForeignKey(User,null=True,blank=True)
	name = models.CharField(max_length=128)
	ip = models.IPAddressField(null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	
	def __unicode__(self):
		return self.name

class Operator(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.first_name
