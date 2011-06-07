#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from django.db import models
#from django.utils.html import escape
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic
#from rapidsms.models import ExtensibleModelBase


class Patient(models.Model):
    """
    This model represents a patient who has registered for PACT.
    """
    number = models.CharField(max_length=15)