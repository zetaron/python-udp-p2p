#from p2p.Handlers.Handler import Handler
from p2p.Handlers import *

class MessageHandler(Handler):
	def onEnable(self):
		self.register(2,self.onMessage)
		
	def setOutput(self,func):
		self.callback = func
		
	def onMessage(self, packet):
		self.callback(packet.connection, packet.data)
	
	
