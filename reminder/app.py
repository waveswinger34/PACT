# vim: ai sts=4 sw=4 ts=4 et
import rapidsms
import re
from models import *
from datetime import datetime
from utils import *

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
                  network=self._network(msg.peer))
        sms.save()

        subject = Subject.objects.filter(phone_number=msg.peer)
        
        
        if not subject:
            subject = Subject(phone_number=msg.peer)
            subject.save()
            msg.respond('Thanks for registering.')
            
            if len(Subject.objects.all()) % 2 is 0:
                pass
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
    
    def _network(self, phone_number):
        xs = phone_number[:3]
        if xs == '026':
            return AIRTEL
        elif xs == '024' or xs == '054':
            return MTN
        elif xs == '020':
            return VODAFONE
        elif xs == '027' or xs == '057':
            return TIGO
        elif xs == '028':
            return EXPRESSO
        else:
            return 'Unknown'
        