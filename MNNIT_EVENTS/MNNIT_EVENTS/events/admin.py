from django.contrib import admin
from .models import events,query,collegeName,campusAmbassador,ticket

# Register your models here.
admin.site.register(events)
admin.site.register(query)
admin.site.register(collegeName)
admin.site.register(campusAmbassador)
admin.site.register(ticket)