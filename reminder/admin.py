#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.contrib import admin
from models import *

#class ConnectionInline(admin.TabularInline):
#    model = Connection
#    extra = 1

class SMSAdmin(admin.ModelAdmin):
    list_display = ('sender', 'received_at', 'text', 'network',) 

admin.site.register(SMS, SMSAdmin)
admin.site.register(Subject)
