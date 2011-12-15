from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.conf.urls.defaults import *
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from chat.forms import MessageForm, InformationForm
from django.views.decorators.csrf import csrf_exempt
from chat.models import Message, Chat, Visitor, Operator, Department
from django.shortcuts import redirect
from django.utils import simplejson
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import time

@csrf_exempt
def start_chat(request):

    form = InformationForm()
    
    if request.POST:
            chat = Chat()
            form = InformationForm(request.POST)

    if form.is_valid():
            try:
                operator = Operator.objects.get(id=1)
            except Operator.DoesNotExist:
                raise

            try:
                user = User.objects.get(id=1)
            except User.DoesNotExist:
                raise
            try:
                department = Department.objects.get(id=1)
            except Department.DoesNotExist:
                raise
            visitor = Visitor(first_name=form.cleaned_data['first_name'])
            visitor.save()
            chat = Chat(operator=operator,department=department, status='4')
            chat.save()
	    return HttpResponseRedirect('/chat/view/%s/' % (chat.id))

    return render_to_response('chat/start_chat.html', {"form": form})


@csrf_exempt
def add_message(request, chat_id):
	form = MessageForm
	error = {}

	try:
		chat = Chat.objects.get(id=chat_id)
	except Chat.DoesNotExist:
		raise

	if request.method == "POST":
		form = MessageForm(request.POST)

		if form.is_valid():
			f = form.save(commit=False)
			f.ip = "1.2.3.4"
			f.chat = chat
			f.save()

			if request.is_ajax():
				error['error'] = 'False'
				return HttpResponse(simplejson.dumps(error))
			else:
				return redirect('/messages/%s/' % (f.chat.id))


def view_chat(request, chat_id):
	form = MessageForm
	try:
		chat = Chat.objects.get(id=chat_id)
	except    Chat.DoesNotExist:
		raise
	return render_to_response('chat/add_message.html', {"form": form, "chat": chat})

@login_required
def view_messages(request, chat_id):
	try:
		messages = Message.objects.filter(chat__id=chat_id).order_by('date_sent')
	except Message.DoesNotExist:
		raise

	if request.is_ajax():
		message_list = []
		for message in messages:
			message_dict = {'body': message.body,
							'ip': message.ip,
							'message_from': message.message_from,
							'date_sent': message.date_sent.strftime("%I:%M %p")}
			message_list.append(message_dict)
		return HttpResponse(simplejson.dumps(message_list))

	return render_to_response('chat/see_chat.html', {"messages": messages})


@login_required
def view_chat_list(request):
    try:
        chats = Chat.objects.filter(status='4')
    except Chat.DoesNotExist:
        raise

    if request.is_ajax():
        active_chats = []
        for chat in chats:
            chat_dict = { 'title' : chat.title,
                             'id': chat.id }
            active_chats.append(chat_dict)
        return HttpResponse(simplejson.dumps(active_chats))

    return render_to_response('chat/view_chat_list.html', {"chats": chats})

#def take_chat()