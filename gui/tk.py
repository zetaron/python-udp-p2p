import sys
from tkinter import *
from tkinter import ttk
from p2p import *

class TkGui(Tk):
    def __init__(self, p2p):    
        Tk.__init__(self)
        self.p2p = p2p
        self.peers = {}
        self.nickname = "v0rtex"
        
    def start(self):
        self.title("Simple P2P Chat")
        
        menubar = Menu(self)
        menubar.add_command(label="Add peer", command=self.addPeer)
        menubar.add_command(label="Set Nick", command=self.setNickname)
        self.config(menu=menubar)
        
        self.resizable(width=FALSE, height=FALSE)
        
        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0)
        mainframe.grid_columnconfigure(0, weight=1)
        mainframe.grid_rowconfigure(0, weight=1)

        self.chat = Text(mainframe, width=50, state="disabled")
        
        self.chat.tag_configure('answer', foreground='red', font=('Verdana', 10))
        self.chat.tag_configure('normal', foreground='blue', font=('Verdana', 10, 'italic'))
         
        self.chat.grid(column=0, row=0, columnspan=2, sticky=(N,E,W,S))
       
        self.scroll = ttk.Scrollbar(mainframe, orient=VERTICAL, command=self.chat.yview)
        self.scroll.grid(column=2, row=0, sticky=(N,S))
        
        self.chat.configure(yscrollcommand=self.scroll.set)
        
        self.eingabe = ttk.Entry(mainframe)
        self.eingabe.grid(column=0, row=1, sticky=(W,E))
        self.eingabe.bind('<Return>', self.send)
        
        self.btn_send = ttk.Button(mainframe, text='Send', command=self.send)
        self.bind('<Destroy>', self.shutdown)
        
        self.btn_send.grid(column=1, row=1, columnspan=2)
        
        #self.peers = StringVar()
        self.peerlist = Listbox(mainframe) #listvariable=self.peers
        self.peerlist.grid(column=3, row=0, sticky=(N,W,S,E))
        
        self.mainloop()
        
    def addMessage(self, name, msg):
        self.addText("{0}: {1}".format(name, msg), "answer")
        
    def addPeer(self):
        self.peerdialog = Toplevel(self)
        self.peerdialog.title("Add a ip please")
        self.peerdialog.resizable(width=FALSE, height=FALSE)  
        self.peeraddr = ttk.Entry(self.peerdialog, width=30)
        self.peeraddr.grid(column=0, row=0, sticky=(W, E))
        
        ttk.Button(self.peerdialog, text='Add', command=self.addPeerAction).grid(column=1, row=0, sticky=(W, E))
        
    def setNickname(self):
        self.nickdialog = Toplevel(self)
        self.nickdialog.title("Set your nickname")
        self.nickdialog.resizable(width=FALSE, height=FALSE)  
        self.nick = ttk.Entry(self.nickdialog, width=30)
        self.nick.grid(column=0, row=0, sticky=(W, E))
        
        ttk.Button(self.nickdialog, text='Set', command=self.setNick).grid(column=1, row=0, sticky=(W, E))
        
    def setNick(self):
        self.nickname = self.nick.get()
        self.nickdialog.destroy()

    def addPeerAction(self):
        self.p2p.send(Packet((self.peeraddr.get(), 3333), 3, self.nickname)) #TODO: add Input validation!!!
        self.peerdialog.destroy()
        
    def addList(self,name):
        self.peerlist.insert(END,name)
        
    def send(self, *args):
        self.addText("You: {0}".format(self.eingabe.get()))
        
        eingabe = self.eingabe.get()
        
        for peer_id in self.peers:
            peer = self.peers[peer_id]
            packet = p2p.Packet(peer.address, p2p.Types.MESSAGEHANDLER, "{0}:{1}".format(self.nickname,eingabe))
            self.p2p.send(packet)
        self.eingabe.delete(0, END)
        
    def addText(self, text, tag = 'normal'):
        self.chat.configure(state="normal")
        self.chat.insert(END, text + "\n", tag)
        self.chat.configure(state="disabled")
        
    def shutdown(self, *args):
        self.p2p.close()
        self.destroy()
        sys.exit(0)