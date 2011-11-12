#from p2p.Handlers.Handler import Handler
from p2p.Handlers import *

class MessageHandler(Handler):
    def onEnable(self, p2p, chat):
        self.chat = chat
        self.register(2,self.onMessage)

    def onMessage(self, packet):
        peerdata = packet.data.split(':', 1)
        self.chat.addMessage(peerdata[0], peerdata[1])
	
	
