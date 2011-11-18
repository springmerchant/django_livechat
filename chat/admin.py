from chat.models import Chat
from chat.models import Message
from chat.models import Department
from chat.models import Operator,Visitor
from django.contrib import admin


admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Department)
admin.site.register(Operator)
admin.site.register(Visitor)


