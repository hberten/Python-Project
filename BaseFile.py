from tkinter import *

root = Tk()
root.configure(background='black')
term_stringvar = StringVar()
definition_stringvar = StringVar()


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.textbox = Text(master, height=1, width=20)
        self.grid()
        self.create_widgets()
        pad = 3
        self._geom = '750x500+0+0'
        master.geometry('{0}x{1}+0+0'.format(master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def create_widgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=2)
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        top.columnconfigure(1, weight=1)
        top.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        Label(self, background='grey', fg='white', text='Term', padx=5).grid(row=0, column=0)
        Entry(self, textvariable=term_stringvar).grid(row=0, column=1)
        Label(self, background='grey', fg='white', text='Definition', padx=5).grid(row=0, column=2)
        Entry(self, textvariable=definition_stringvar).grid(row=0, column=3)
        save_button = Button(self, background='grey', fg='white', text='Save', padx=5)
        save_button.configure(command=self.flashcard_save)
        save_button.grid(row=1, column=0)

    def textbox_print(self):
        if self.textbox.get('1.0', END).lower() == 'correct\n':
            print('Yep')
        else:
            print('Nope')

    def flashcard_save(self):
        flashcard_file = open('flashcard_file.txt', 'w')
        flashcard_file.write(str(term_stringvar.get() + ': ' + definition_stringvar.get()))
        flashcard_file.close()


app = Application(root)
app.mainloop()
