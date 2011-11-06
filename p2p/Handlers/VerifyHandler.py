from p2p.Handlers import *

class VerifyHandler(Handler):
	def handle(self, packet):
		toHandle = self.getSentPacket(packet)
		toHandle.verified = True
		print("YOU ARE LEGAL!!")
		
	def onEnable(self):
		self.register(1,self.handle)
		
