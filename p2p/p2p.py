import queue, socket
from p2p import *
#from p2p.Packet import Packet

#from p2p.ReceiveThread import ReceiveThread
#from p2p.SendThread import SendThread
#from p2p.WatchThread import WatchThread

#from p2p.Handlers.Handler import Handler
#from p2p.Handlers.VerifyHandler import VerifyHandler

#from p2p.Types import Types

class P2P(object):
	def __init__(self, peers = [], port = 3333):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(('', port))
		
		self.peerlist = peers
		self.packetHandler = {}		#{1:[callback1,callback2],2:[callback4],3:[callback1,callback4]}
		self.send_queue = queue.Queue()
		self.out_queue = queue.Queue()
		self.data_out = []

		self.receiveThread = ReceiveThread(self.sock, self)
		self.sendThread = SendThread(self.sock, self.send_queue, self.out_queue, self.data_out)
		self.watchThread = WatchThread(self.out_queue, self.send_queue, self.data_out)
		
		self.receiveThread.start()
		self.sendThread.start()
		self.watchThread.start()
		
		self.addHandler(VerifyHandler(self))
		self.addHandler(HandshakeHandler(self))

	def stop(self):
		self.receiveThread.stop()
		self.sendThread.stop()
		self.watchThread.stop()
	
	def close(self):
		self.stop()
	
	def __del__(self):
		self.stop()
	
	def addHandler(self, handler):
		handler.onEnable()

	def handle(self, packet):
		if packet.handlerId in self.packetHandler:
			for callback in self.packetHandler[packet.handlerId]:
				callback(packet)
	
	def send(self, packet):
		self.send_queue.put(packet)
	
		
		
		
		
