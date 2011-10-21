import queue, socket
from Packet import Packet

from ReceiveThread import ReceiveThread
from SendThread import SendThread
from WatchThread import WatchThread

from Handlers.Handler import Handler
from Handlers.VerifyHandler import VerifyHandler

from Types import Types

class P2P(object):
	def __init__(self, connections = [], port = 3333):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(('', port))
		
		self.connections = connections
		self.handler = {}
		self.send_queue = queue.Queue()
		self.out_queue = queue.Queue()
		self.data_out = []

		self.receiveThread = ReceiveThread(self.sock, self)
		self.sendThread = SendThread(self.sock, self.send_queue, self.out_queue, self.data_out)
		self.watchThread = WatchThread(self.out_queue, self.send_queue, self.data_out)
		
		self.receiveThread.start()
		self.sendThread.start()
		self.watchThread.start()
		
		self.addHandler(Types.VERIFYHANDLER, VerifyHandler(self))

	def stop(self):
		self.receiveThread.stop()
		self.sendThread.stop()
		self.watchThread.stop()
	
	def __del__(self):
		self.stop()
	
	def addHandler(self, handlerId, handler):
		self.handler[handlerId] = handler
		
	def handle(self, packet):
		if self.handler[packet.handlerId]:
			self.handler[packet.handlerId].handle(packet)
	
	def send(self, packet):
		self.send_queue.put(packet)
	
		
		
		
		