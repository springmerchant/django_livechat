from django import forms
from chat.models import Message
from chat.models import Chat

class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ('body', 'ip', 'chat', 'visitor', 'operator')
