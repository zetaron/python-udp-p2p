#from p2p.Handlers.Handler import Handler
from p2p.Handlers import *

class MessageHandler(Handler):
	def handle(self, packet):
		print("{0}/{1} [SENT] : {2}".format(packet.connection[0], packet.connection[1], packet.data))
