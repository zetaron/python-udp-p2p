#from p2p.Packet import Packet

class Handler(object):
	def __init__(self, p2p):
		self.p2p = p2p
		
	def onEnable(self):
		pass
		
	def register(self, id, callback):
			if id in self.p2p.packetHandler:
				self.p2p.packetHandler[id].append(callback)
			else:
				self.p2p.packetHandler[id] = [callback]
		
	def getSentPacket(self, packet):
		for pkt in self.p2p.data_out:
			if pkt.hash == packet.data:
				return pkt