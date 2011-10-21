import p2p
from Handlers.MessageHandler import MessageHandler

myp2p = p2p.P2P([("127.0.0.1", 2222)])
myp2p.addHandler(p2p.Types.MESSAGEHANDLER, MessageHandler(myp2p))
myp2p.send(p2p.Packet(("127.0.0.1", 2222), p2p.Types.MESSAGEHANDLER, "Hi there!"))