from p2p.Handlers import *

#Packet101: Handshake

class HandshakeHandler(Handler):
	def onEnable(self):
		self.register(3,self.handleHandshake)
		
	def handleHandshake(self, packet):
		print("Test\n")
		
	
		
