import socket, queue, threading, time
from Packet import Packet
from Types import Types

class SendThread(threading.Thread):
	def __init__(self, socket, send_queue, out_queue, data_out):
		self.socket = socket
		self.send_queue = send_queue
		self.out_queue = out_queue
		self.data_out = data_out
		
		threading.Thread.__init__(self)
		
	def stop(self):
		self.running = 0
		
	def run(self):
		self.running = 1
		while self.running:
			packet = self.send_queue.get(True)
			self.socket.sendto(packet.pack(), packet.connection)
			if packet.handlerId != Types.VERIFYHANDLER:
				packet.last_sent = time.time()
				packet.tries += 1
				self.out_queue.put(packet)
				self.data_out.append(packet)
			
		
		
		