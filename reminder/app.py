# vim: ai sts=4 sw=4 ts=4 et
import rapidsms
import re
from models import *
from utils import *

from rapidsms.contrib.scheduler.models import EventSchedule, ALL
from datetime import datetime, timedelta

import random

class App(rapidsms.apps.base.AppBase):
#    def __init__(self, router):
#        AppBase.__init__(self, router)
        
    def start (self):
        """Configure your app in the start phase."""
        pass

    def parse (self, message):
        """Parse and annotate messages in the parse phase."""
        pass

    def handle (self, msg):
        sms = SMS(received_at=msg.date,
                  sender=msg.peer,
                  text=msg.text,
                  network=network(msg.peer))
        sms.save()

        subject = Subject.objects.filter(phone_number=msg.peer)
        

        schedule = EventSchedule.objects.all()
        if not schedule:
            EventSchedule(callback='reminder.tasks.broadcast',
                          minutes=ALL, 
                          start_time=datetime.now() + timedelta(minutes=1),
                          end_time=datetime.now() + timedelta(minutes=2)).save()

        if not subject:
            subject = Subject(phone_number=msg.peer,
                              received_at=msg.date)
            
            if len(Subject.objects.all()) % 2 is 0:
                subject.message_id = random.randint(0, 2)
            subject.save()
            msg.respond('Thanks for registering.')
            return True
        elif msg.text.lower() is 'stop' and subject.active:
            subject.active = False
            subject.save()
            msg.response('You have been removed from PACT')
            return True
        else:
            msg.respond("You are already registered. To stop receiving messages, text STOP. Thanks")
            return True
        
    def cleanup (self, message):
        """Perform any clean up after all handlers have run in the
           cleanup phase."""
        pass

    def outgoing (self, message):
        """Handle outgoing message notifications."""
        pass

    def stop (self):
        """Perform global app cleanup when the application is stopped."""
        pass
        