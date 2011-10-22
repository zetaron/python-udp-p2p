import hashlib, struct

class Packet(object):
	def __init__(self, connection, handlerId, data):
		self.connection = connection
		self.handlerId = handlerId
		self.data = data
		self.tries = 0
		self.last_sent = 0
		self.verified = False
		self.hash = hashlib.sha224(self.pack()).hexdigest()
		
	def pack(self):
		return (struct.pack(">h", self.handlerId) + str(self.data).encode())