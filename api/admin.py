from django.contrib import admin
from .models import Agent
from .models import Event
from .models import Group
from .models import GroupUser
from .models import User
from django.apps import apps


admin.site.register(Agent)
admin.site.register(Event)
admin.site.register(GroupUser)
admin.site.register(User)
admin.site.register(Group)
