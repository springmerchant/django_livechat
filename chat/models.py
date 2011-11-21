from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
	start_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	operator = models.ForeignKey('Operator')
	end_date = models.DateTimeField()
	department = models.ForeignKey('Department',null=True,blank=True)
	visitor = models.ForeignKey('Visitor')
	def __unicode__(self):
		return self.title


class Message(models.Model):
	body = models.TextField()
	date_sent = models.DateTimeField(auto_now=True)
	date_edited = models.DateTimeField(null=True,blank=True)
	ip = models.IPAddressField()
	chat = models.ForeignKey(Chat)
	visitor = models.ForeignKey('Visitor')
	operator = models.ForeignKey('Operator')
	def __unicode__(self):
		return self.chat.title

class Department(models.Model):
	name = models.CharField(max_length=128)
	operators = models.ManyToManyField('Operator')
	def __unicode__(self):
		return self.name
<<<<<<< HEAD

class Visitor(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=128, null=True)
	ip = models.IPAddressField(null=True)
	email = models.EmailField(null=True)
=======
		

class Visitor(models.Model):
	user = models.ForeignKey(User,null=True,blank=True)
	name = models.CharField(max_length=128)
	ip = models.IPAddressField(null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
>>>>>>> 9768a04ef24e3912211f0c9368aac0ac0251e33e
	def __unicode__(self):
		return self.name
		
class Operator(models.Model):
<<<<<<< HEAD
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	def __unicode__(self):
		return self.first_name
=======
	user = models.ForeignKey(User,null=True,blank=True)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	def __unicode__(self):
		return self.first_name
>>>>>>> 9768a04ef24e3912211f0c9368aac0ac0251e33e
