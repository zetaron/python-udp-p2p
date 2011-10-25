from p2p import *

myp2p = P2P()
myp2p.addHandler(p2p.Types.MESSAGEHANDLER, p2p.Handlers.MessageHandler(myp2p))

myp2p.send(Packet(("5.148.251.77", 3333), p2p.Types.MESSAGEHANDLER, "Hi zetaron !!! XD "))
