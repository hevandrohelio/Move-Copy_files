from tkinter import *
import move_copy

root = Tk()
class App():
    def __init__(self):
        self.root = root
        self.window()
        self.origin_new_dir()
        root.mainloop()

    def window(self):
        self.root.title('Copiar ou Mover arquivos')
        self.root.geometry('720x600')
        self.root.resizable(False, False)

    def origin_new_dir(self):
        # Select Origin directory btn
        self.btn_odir = Button(self.root, text='Origin Directory')
        self.btn_odir.place(relx=0.8, rely=0.1, relwidth=0.15, relheight=0.05)

        # Select New Directory btn
        self.btn_ndir = Button(self.root, text='New Directory')
        self.btn_ndir.place(relx=0.8, rely=0.18, relwidth=0.15, relheight=0.05)

        # Copy btn
        self.copy_btn = Button(self.root, text='Copy files')
        self.copy_btn.place(relx= 0.3, rely = 0.9, relwidth=0.15, relheight=0.05)

        # Move btn
        self.move_btn = Button(self.root, text='Move files')
        self.move_btn.place(relx=0.6, rely=0.9, relwidth=0.15, relheight=0.05)

        # Origin directory Entry
        self.etr_odir = Entry(self.root)
        self.etr_odir.place(relx=0.1, rely=0.1, relwidth=0.68, relheight=0.05)

        # New Directory Entry
        self.etr_ndir = Entry(self.root)
        self.etr_ndir.place(relx=0.1, rely=0.18, relwidth=0.68, relheight=0.05)


App()
