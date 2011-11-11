from p2p.Handlers import *

class VerifyHandler(Handler):
	def onEnable(self, p2p):
		self.register(1,self.handle)
		
	def handle(self, packet):
		toHandle = self.getSentPacket(packet)
		toHandle.verified = True
		print("ACK:{0}".format(toHandle.handlerId))