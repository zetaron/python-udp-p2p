import socket, threading, struct, select
from p2p import *
#from p2p.Packet import Packet
#from p2p.Types import Types

class ReceiveThread(threading.Thread):
	def __init__(self, sock, p2p):
		self.sock = sock
		self.p2p = p2p
		
		threading.Thread.__init__(self)
    
	def stop(self):
		self.running = 0
    
	def run(self):
		self.running = 1
		while self.running:
			inputready,outputready,exceptready = select.select([self.sock],[],[])
			for sock in inputready:
				data, addr = sock.recvfrom(1024)
				handlerId, = struct.unpack(">h", data[:2])
				pkt_data = str(data[2:],"UTF-8")
				packet = Packet(addr, handlerId, pkt_data)
				
				if packet.handlerId != Types.VERIFYHANDLER:
					self.p2p.send(Packet(addr, Types.VERIFYHANDLER, packet.hash))
                
				self.p2p.handle(packet)
		

				
				

		
	


