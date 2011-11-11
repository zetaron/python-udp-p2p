#from p2p.Handlers.Handler import Handler
from p2p.Handlers import *

class MessageHandler(Handler):
    def onEnable(self, p2p, chat):
        self.chat = chat
        self.register(2,self.onMessage)

    def onMessage(self, packet):
        self.chat.addMessage(packet.address, packet.data)
	
	
