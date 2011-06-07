# vim: ai sts=4 sw=4 ts=4 et
import rapidsms
import re
from models import *
from datetime import datetime

class App(rapidsms.apps.base.AppBase):
    def start (self):
        """Configure your app in the start phase."""
        pass

    def parse (self, message):
        """Parse and annotate messages in the parse phase."""
        pass

    def handle (self, message):
        if True:
            message.respond('Thank you for registering!')
            return True
        return False

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