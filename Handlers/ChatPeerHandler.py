from p2p.Handlers import *
from p2p.Peer import *

class ChatPeerHandler(Handler):
    def onEnable(self, p2p, chat):
        self.chat = chat
        self.p2p = p2p
        self.register(3,self.onPeerHandshakePacket)
        
    def onPeerHandshakePacket(self, packet):
        peer = Peer(packet.address, packet.data)
        
        if(peer.id in self.chat.peers):
            print("Peer already in peerlist.")
        else:
            print("New Peer: {0}".format(peer.id))
            self.chat.peers[peer.id] = peer
            self.chat.addList(peer.id)
            self.p2p.send(Packet(("127.0.0.1", 3333), 3, "Vincent"))