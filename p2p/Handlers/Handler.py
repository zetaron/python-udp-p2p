#from p2p.Packet import Packet

class Handler(object):
	def __init__(self, p2p):
		self.p2p = p2p

	def handle(self, packet):
		pass
		
	def getSentPacket(self, packet):
		for pkt in self.p2p.data_out:
			if pkt.hash == packet.data:
				return pkt
