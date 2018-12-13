# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 21:53:38 2018

@author: User
"""

from fbchat import Client, log
from fbchat.models import *

import credentials

class BotStar(Client):
    def onMessage( self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs ):
        self.markAsRead(author_id)
        
        log.info("Message{} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = messsage_object.text
        
        reply = "Hello!"
        
        if author_id!=self.uid:
            self.send(Message(text=reply),thread_id=thread_id, thread_type=thread_type)
            
        self.markAsDelivered(author_id, thread_id)    
 
client = BotStar(credentials.email, credentials.password)           
        
        
