from tkinter import *
import json

root = Tk()
root.configure(background='black')


class Application(Frame):
    current_row = 0
    entry = None
    dictionary = {}

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        # pad = 20
        # self._geom = '750x500+0+0'
        # master.geometry('{0}x{1}+0+0'.format(master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        # master.bind('<Escape>', self.toggle_geom)

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

        self.create_row()

    def textbox_print(self):
        if self.textbox.get('1.0', END).lower() == 'correct\n':
            print('Yep')
        else:
            print('Nope')

    def create_row(self, key = None):

        if 'TermEntry'+str(self.current_row) in self.dictionary:
            self.dictionary['TermEntry'+str(self.current_row)].unbind('<Key>')
            self.dictionary['DefinitionEntry'+str(self.current_row)].unbind('<Key>')
            self.current_row += 1

        Label(self, background='grey', fg='white', text='Term', padx=5).grid(row=self.current_row, column=0)

        term_entry = Entry(self) # creates the term entry box for the line
        term_entry.bind('<Key>', self.create_row) # binds the create_row function to run when something is typed
        term_entry.grid(row=self.current_row, column=1)
        self.dictionary['TermEntry'+str(self.current_row)] = term_entry # places term_entry in the dictionary

        Label(self, background='grey', fg='white', text='Definition', padx=5).grid(row=self.current_row, column=2)

        definition_entry = Entry(self) # creates the definition entry box for the line
        definition_entry.bind('<Key>', self.create_row)  # binds the create_row function to run when something is typed
        definition_entry.grid(row=self.current_row, column=3)
        self.dictionary['DefinitionEntry'+str(self.current_row)] = definition_entry  # places definition_entry in dictionary

        save_button = Button(self, background='grey', fg='white', text='Save', padx=5)
        save_button.configure(command=self.flashcard_save)
        save_button.grid(row=self.current_row+1, column=0)

    def flashcard_save(self):
        flashcard_file = open('flashcard_file.json', 'w')
        current_row = self.current_row
        term_dictionary = {}
        for row in range(0, current_row):
            row = str(row)
            term_dictionary[self.dictionary['TermEntry'+row].get()] = self.dictionary['DefinitionEntry'+row].get()
        json.dump(term_dictionary, flashcard_file)
        flashcard_file.close()


app = Application(root)
app.mainloop()