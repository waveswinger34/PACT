# vim: ai sts=4 sw=4 ts=4 et
import rapidsms
import re
from models import *
from datetime import datetime

class App(rapidsms.apps.base.AppBase):
    def __init__(self, router):
#        super(App, router)
        self.router = router
        self.register = {}
        self.count = 0
        
        
    def start (self):
        """Configure your app in the start phase."""
        pass

    def parse (self, message):
        """Parse and annotate messages in the parse phase."""
        pass

    def handle (self, msg):
        print 'Message date is: %s' % msg.date
        
        if msg.peer not in self.register:
#            self.register.append(msg)
            self.register[msg.peer] = msg
#            msg.respond('Thanks for registering.')
#            self.modem.send_sms(msg.sender, "Thanks for registering.")
#            self.modem.wait_for_network()
#            if self.count % 2 is 0:
#                self.scheduler.add(msg)
#            self.count += 1
            return True
        elif msg.text.lower() is 'stop':
            print 'OK OK we get it!'
            #TODO
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