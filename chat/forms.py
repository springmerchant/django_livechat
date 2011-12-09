from django import forms
from chat.models import Message
from chat.models import Chat
from chat.models import Department

class MessageForm(forms.ModelForm):
	body = forms.CharField(label='Message',widget=forms.Textarea(attrs={'class':'message_body'}))
	class Meta:
		model = Message
		fields = ('body', )
		
class InformationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    question = forms.CharField()