#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import time
from pygsm import GsmModem

class Reminder(object):
    register = []
    
    def __init__(self, modem):
        self.modem = modem

    def serve(self):
        while True:
            print "Checking for message..."
            msg = self.modem.next_message()

            if msg is not None:
                self.handle(msg)
            time.sleep(2)

    def handle(self, msg):
        # check if sender in database
        if msg.sender not in self.register:
            self.register.append(msg.sender)
            msg.respond("Thanks for registering.")
        elif msg.text.lower() is 'stop':
            print 'OK OK we get it!'
            #TODO
        else:
            # just log the message
            pass    

    def handle_registration(self):
        pass
    

port = '/dev/tty.airtel'

gsm = GsmModem(
    port=port,
    logger=GsmModem.debug_logger).boot()

print "Waiting for network..."
s = gsm.wait_for_network()

# start the demo app
app = Reminder(gsm)
app.serve()

#gsm.send_sms('0245014728', 'wohoooo!!')
