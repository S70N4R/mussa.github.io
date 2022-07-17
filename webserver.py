
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tokenize import String
from http.server import HTTPServer, CGIHTTPRequestHandler
import os
import threading


class WebServer(ttk.Frame):
    def __init__(self, parent=None):
        ttk.Frame.__init__(self, parent)
        self.appname = "PyWebserver"
        self.master.title(self.appname)
        self.master.resizable(False, False)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.serverDir = StringVar()
        self.portNum = IntVar(value=80)
        self.label = StringVar()
        self.server_gui()

    def server_gui(self):
        srvr_lab = ttk.Label(self, text="Server dir:")
        port_lab = ttk.Label(self, text="Port Number:")
        srvr = ttk.Entry(self, width=60, textvariable=self.serverDir)
        port = ttk.Entry(self, width=60, textvariable=self.portNum)
        start_srvr = ttk.Button(self, text="Start", command=self.start)
        browse_dir = ttk.Button(self, text="Browse", command=self.browse)
        info = ttk.Label(self, relief=GROOVE, textvariable=self.label)

        srvr_lab.grid(column=0, row=0, sticky=W)
        port_lab.grid(column=0, row=1,  sticky=W)
        srvr.grid(column=1, row=0, columnspan=2, sticky=(W, E), pady=3, padx=2)
        port.grid(column=1, row=1, sticky=(W, E), pady=3, padx=2)
        # info.grid(column=1, row=2, sticky=(W, E), ipady=7)
        browse_dir.grid(column=2, row=1, sticky=E)
        start_srvr.grid(column=2, row=2, sticky=E)

    def browse(self):
        dir = askdirectory(title=self.appname)
        if dir:
            self.serverDir.set(dir)

    def start(self):
        message = "Webserver Dir-> %s\nPort Number-> %s"
        def run():
            os.chdir(self.serverDir.get())
            server_dir = ("", self.portNum.get())
            server_object = HTTPServer(server_dir, CGIHTTPRequestHandler)
            self.label.set(message % (self.serverDir.get(), self.portNum.get()))
            print(self.label.get())
            server_object.serve_forever()
        thread = threading.Thread(target=run)
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    WebServer().mainloop()
