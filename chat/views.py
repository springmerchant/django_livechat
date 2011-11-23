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
from chat.models import Message
from django.shortcuts import redirect
from django.utils import simplejson

@csrf_exempt
def message(request):
	form = MessageForm
	error = {}
	
	if request.method == "POST":
		form = MessageForm(request.POST)
	
		if form.is_valid():
		
			f = form.save(commit=False)
			f.ip = "1.2.3.4";
			
			f.save()
			
			if request.is_ajax():
				error['error'] = 'False'
				return HttpResponse(simplejson.dumps(error))
			else:
				return redirect('/messages/%s/'% (f.chat.id))

	return render_to_response('chat/add_message.html',{"form":form})	

	
	

def view_messages(request, chat_id):
	try:
		messages = Message.objects.filter(chat__id=chat_id)
	except Message.DoesNotExist:
		raise
	
	return render_to_response('chat/see_chat.html',{"messages":messages})