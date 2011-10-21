import socket, threading, struct, select

from Packet import Packet
from Types import Types

class ReceiveThread(threading.Thread):
	def __init__(self, socket, p2p):
		self.socket = socket
		self.p2p = p2p
		
		threading.Thread.__init__(self)
    
	def stop(self):
		self.running = 0
    
	def run(self):
		self.running = 1
		while self.running:
			inputready,outputready,exceptready = select.select([self.socket],[],[],5)
			for sock in inputready:
				data, addr = sock.recvfrom(1024)
				handlerId, = struct.unpack(">h", data[:2])
				pkt_data = str(data[2:],"UTF-8")
				packet = Packet(addr, handlerId, pkt_data)
				
				if packet.handlerId != Types.VERIFYHANDLER:
					self.p2p.send(Packet(addr, Types.VERIFYHANDLER, packet.hash))
				
				# Implement handler callback
				self.p2p.handle(packet)
		

				
				

		
	


