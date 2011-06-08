#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.router import router
import logging
from reminder.models import Subject
from reminder.utils import MSGS
from django.db.models.query import Q
from rapidsms.models import Connection
from rapidsms.messages.outgoing import OutgoingMessage

def broadcast(router):

    print '>>>>>>>>> broadcastingadg;fklas'
    backend = router.backends['airtel']
    subjects = Subject.objects.filter(Q(messages_left__gt=0)|
                                      Q(active=True))
    
    for subject in subjects:
        OutgoingMessage(connection=gsm_connection(identity=subject.phone_number),
                        text=MSGS[subject.message_id]).send()        
        subject.messages_left -= 1
        subject.save()
        logging.debug('wohoooo')
        
        
def gsm_connection(name='airtel', identity='0266688206'):
    
    backend = router.backends[name]
    # ensure that a persistent connection instance exists for this
    # backend+identity pair. silently create one, if not.
    conn, created = Connection.objects.get_or_create(backend=backend, 
                                                     identity=identity)
    return conn
