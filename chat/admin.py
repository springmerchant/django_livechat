from chat.models import Chat
from chat.models import Message
from chat.models import Department
from chat.models import Visitor
from chat.models import Operator
from django.contrib import admin


admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Department)
admin.site.register(Visitor)
admin.site.register(Operator)


