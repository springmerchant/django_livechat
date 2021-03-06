from django.db import models
from django.contrib.auth.models import User


CHAT_STATUS = (
        (1, 'Closed'),
        (2, 'Timed Out'),
		(3, 'Unanswered'),
		(4, 'Active')
    )
class Chat(models.Model):
	start_date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=256)
	operator = models.ForeignKey('Operator',null=True,blank=True)
	end_date = models.DateTimeField(null=True,blank=True)
	department = models.ForeignKey('Department',null=True,blank=True)
	visitor = models.ForeignKey('Visitor',null=True,blank=True)
	status = models.PositiveSmallIntegerField(max_length=2, choices=CHAT_STATUS)
	
	def __unicode__(self):
		return self.title

class Message(models.Model):
	body = models.TextField()
	date_sent = models.DateTimeField(auto_now=True)
	date_edited = models.DateTimeField(null=True,blank=True)
	ip = models.IPAddressField()
	chat = models.ForeignKey(Chat)
	visitor = models.ForeignKey('Visitor',null=True,blank=True)

	def get_from(self):
		if self.visitor:
			return "%s" % self.chat.visitor.first_name
		else:
			return "%s" % self.chat.operator.first_name

	def __unicode__(self):
		return self.chat.title

class Department(models.Model):
	name = models.CharField(max_length=128)
	operators = models.ManyToManyField('Operator')
	
	def __unicode__(self):
		return self.name



class Visitor(models.Model):
	user = models.ForeignKey(User,null=True,blank=True)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	ip = models.IPAddressField(null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	
	def __unicode__(self):
		return self.first_name

class Operator(models.Model):
	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.first_name



