from Handlers.Handler import Handler

class VerifyHandler(Handler):
	def handle(self, packet):
		toHandle = self.getSentPacket(packet)
		toHandle.verified = True
		print("YOU ARE LEGAL!!")
		