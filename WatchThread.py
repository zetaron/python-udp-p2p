import queue, threading, time
from Packet import Packet

class WatchThread(threading.Thread):
	def __init__(self, out_queue, send_queue, data_out):
		self.out_queue = out_queue
		self.send_queue = send_queue
		self.data_out = data_out
		
		threading.Thread.__init__(self)
		
	def stop(self):
		self.running = 0
		
	def run(self):
		self.running = 1
		while self.running:
			packet = self.out_queue.get(True)
			if packet.verified == False:
				if packet.tries < 3:
					if (time.time() - packet.last_sent) >= 3000:
						self.send_queue.put(packet)
						self.data_out.remove(packet)