from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.conf.urls.defaults import *
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from chat.forms import MessageForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def message(request):
	form = MessageForm #<- it is a Form not a Model, it is a Form based on a Model, but still a Form object
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			f=form.save(commit=False)
			f.save()
			
	return render_to_response('chat/add_message.html',{"form":form})
