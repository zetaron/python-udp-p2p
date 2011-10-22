import p2p
import time
from Handlers.MessageHandler import MessageHandler

myp2p = p2p.P2P([("5.148.251.77", 3333)])
myp2p.addHandler(p2p.Types.MESSAGEHANDLER, MessageHandler(myp2p))

myp2p.send(p2p.Packet(("5.148.251.77", 3333), p2p.Types.MESSAGEHANDLER, "Hi zetaron !!! XD "))