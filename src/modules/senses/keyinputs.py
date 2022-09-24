from modules import Memory
from tkinter import Tk, X, StringVar
from tkinter.ttk import Entry, Frame
from tkinter.scrolledtext import ScrolledText

__author__ = 'piper'


class Getcmd(object):
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.root = Tk()

        sw = self.root.winfo_screenwidth()
        w = self.root.winfo_width()
        x = sw-w
        y = 0

        self.root.minsize(width=200, height=100)
        #self.root.geometry("+{0}+{1}".format(x, y))
        self.root.title('Argon')

        frame = Frame(self.root)
        self.screen = ScrolledText(frame, height=10, width=40, foreground='red',
                            background='#222', font=('Monospace', '8'),
                            state='disabled')
        self.screen.pack()

        self.cmd = StringVar()
        self.ask = Entry(frame, textvariable=self.cmd, background='white smoke',
                         foreground='blue')
        self.ask.focus()
        self.ask.bind('<Return>',self.commit)
        self.ask.pack(fill=X)

        frame.pack()
        self.root.resizable(width=False, height=False)
        #self.root.overrideredirect(True)
        self.root.mainloop()

    def commit(self, e):
        self.screen['state'] = 'normal'
        if self.ask.get().startswith('>'):
            coms = self.ask.get()[1:].split()
            command = '%s.%s' % ('self', coms[0])
            filename = coms[1]
            eval(command)(filename)
        else:
            try:
                memory = Memory.Event(self.ask.get(), 'cmd')
                result = memory.recall()
                self.display(result)
            except Exception as e:
                self.display(e)
            self.screen['state'] = 'disabled'
            self.cmd.set('')

    def display(self, text, inset='1.0'):
        self.screen.insert(inset, text)

    def read_file(self, filename):
        with open(filename, 'r') as file:
            for line in file.readlines():
                memory = Memory.Event(line, 'cmd')
                result = memory.recall()
                self.display(result)
