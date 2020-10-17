from django.contrib import admin
from .models import events,query,collegeName,campusAmbassador

# Register your models here.
admin.site.register(events)
admin.site.register(query)
admin.site.register(collegeName)
admin.site.register(campusAmbassador)