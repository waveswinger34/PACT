#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.db import models
#from django.utils.html import escape
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic
#from rapidsms.models import ExtensibleModelBase

class SubjectManager(models.Manager):
    pass

class SMSManager(models.Manager):
    pass


class Subject(models.Model):
    """
    This model represents a subject who has registered for PACT.
    """
    phone_number = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    message_id = models.IntegerField(null=True)
    messages_left = models.IntegerField(null=True)
    received_at = models.DateTimeField()
    
    def __unicode__(self):
        return self.phone_number
    
    objects = SubjectManager()
    
class SMS(models.Model):
    received_at = models.DateTimeField()
    sender = models.CharField(max_length=15)
    text = models.CharField(max_length=140)
    network = models.CharField(max_length=10)
    
    objects = SMSManager()
    
