from django import forms
from chat.models import Message
from chat.models import Chat

class MessageForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class':'message_body'}))
	class Meta:
		model = Message
		fields = ('chat', 'visitor', 'operator', 'body')