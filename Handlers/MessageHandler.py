from Handlers.Handler import Handler

class MessageHandler(Handler):
	def handle(self, packet):
		print("{0}/{1} [SENT] : {2}".format(packet.connection[0], packet.connection[1], packet.data))