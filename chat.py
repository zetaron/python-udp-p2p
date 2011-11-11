from p2p import *
from gui.tk import TkGui
from Handlers.MessageHandler import *
from Handlers.ChatPeerHandler import *

p2p = P2P()
chat = TkGui(p2p)

MsgHandler = MessageHandler(p2p, chat)
p2p.addHandler(MsgHandler)

PeerHandler = ChatPeerHandler(p2p, chat)
p2p.addHandler(PeerHandler)

chat.start()



