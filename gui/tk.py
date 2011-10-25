import sys
from tkinter import *
from p2p import *

class TkGui(Tk):
    def __init__(self, p2p):    
        super(TkGui, self).__init__()
        
        self.p2p = p2p
        
        # (ip, port): username
        self.users = {}
        
        self.setupUi()
        
    def setupUi(self):
        self.title("Simple P2P Chat")
        
        self.top = Frame(self)
        self.chat = Text(self.top, width=90)
        self.chat.pack(side=LEFT, fill=BOTH, expand=YES)
        self.scroll = Scrollbar(self.top)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.chat.yview)
        self.chat.config(yscrollcommand=self.scroll.set)
        self.top.pack(fill=BOTH, expand=YES)
        
        self.eingabe = Entry(self, width=60)
        self.eingabe.pack(side=LEFT, fill=BOTH, expand=YES)
        self.eingabe.bind('<Return>', self.send)
        
        self.btn_send = Button(self, text='Send', command=self.send)
        
        self.btn_quit = Button(self, text='Quit', command=self.quit)
        self.btn_send.pack(side=LEFT, expand=NO)
        self.btn_quit.pack(side=LEFT, expand=NO)
        
        # add the p2p handlers
        self.p2p.addHandler(p2p.Types.MESSAGEHANDLER, p2p.Handlers.MessageHandler(self.p2p))
        
        self.mainloop()

    def addMessage(self, connection, data):
        addText("{0}: {1}".format(self.users[connection], data))
        
    def send(self, *args):
        self.addText("You: {0}".format(self.eingabe.get()))
        packet = p2p.Packet(("127.0.0.1", 3333), p2p.Types.MESSAGEHANDLER, self.eingabe.get())
        self.p2p.send(packet)
        self.eingabe.delete(0, END)
        
    def addText(self, text):
        self.chat.insert(END, text + "\n")
        
    def quit(self):
        self.p2p.close()
        self.destroy()
        super(TkGui, self).quit()
        sys.exit(0)