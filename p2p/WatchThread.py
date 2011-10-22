import queue, threading, datetime
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
				if packet.tries < 4:
					if  (datetime.datetime.now() - packet.last_sent).seconds >= 3:
						self.send_queue.put(packet)
						self.data_out.remove(packet)
					else:
						self.out_queue.put(packet)