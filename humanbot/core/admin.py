from django.contrib import admin
from humanbot.core.models import Human, ConnectedService, HumanUserConnection

admin.site.register(Human)
admin.site.register(ConnectedService)
admin.site.register(HumanUserConnection)
