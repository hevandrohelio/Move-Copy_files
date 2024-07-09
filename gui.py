from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import move_copy

root = Tk()


class App(move_copy.Mc_file, object):
    def __init__(self):
        self.root = root
        self.window()
        self.origin_new_dir()
        root.mainloop()

    def window(self):
        self.root.title('Copiar ou Mover arquivos')
        self.root.geometry('720x600')
        self.root.resizable(False, False)

    def open_origin_folder(self):
        self.origin_path_text = filedialog.askdirectory()
        self.change_origin_entry_text(self.origin_path_text)
        print(self.origin_path_text)

    def open_new_folder(self):
        self.new_path_text = filedialog.askdirectory()
        self.change_new_entry_text(self.new_path_text)
        print(self.new_path_text)

    def scan_folder(self):
        self.origin_path_text = self.etr_odir.get()
        self.new_path_text = self.etr_ndir.get()
        self.lb_m = Label(self.root, text=f'Scanned')
        self.lb_m.place(relx=0.45, rely=0.9)

    def copy_files(self):
        move_copy.Mc_file(self.origin_path_text, self.new_path_text).copy()
        self.is_file_copied()
    def move_files(self):
        move_copy.Mc_file(self.origin_path_text, self.new_path_text).move()
        self.is_file_moved()

    def origin_new_dir(self):
        # Select Origin directory btn
        self.btn_odir = Button(self.root, text='Origin Directory', command=self.open_origin_folder)
        self.btn_odir.place(relx=0.8, rely=0.1, relwidth=0.15, relheight=0.05)

        # Select New Directory btn
        self.btn_ndir = Button(self.root, text='New Directory', command=self.open_new_folder)
        self.btn_ndir.place(relx=0.8, rely=0.18, relwidth=0.15, relheight=0.05)

        # Copy btn
        self.copy_btn = Button(self.root, text='Copy files', command=self.copy_files)
        self.copy_btn.place(relx=0.3, rely=0.9, relwidth=0.15, relheight=0.05)

        # Move btn
        self.move_btn = Button(self.root, text='Move files', command=self.move_files)
        self.move_btn.place(relx=0.6, rely=0.9, relwidth=0.15, relheight=0.05)

        # Scan Files btn
        self.scan_btn = Button(self.root, text='Scan Folder', command=self.scan_folder)
        self.scan_btn.place(relx=0.45, rely=0.8, relwidth=0.15, relheight=0.05)

        # Origin directory Entry
        self.origin_path_text = StringVar(root)

        self.etr_odir = Entry(self.root, textvariable=self.origin_path_text)
        self.etr_odir.pack()
        self.etr_odir.place(relx=0.1, rely=0.1, relwidth=0.68, relheight=0.05)


        # New Directory Entry
        self.new_path_text = StringVar(root)

        self.etr_ndir = Entry(self.root, textvariable=self.new_path_text)
        self.etr_ndir.pack()
        self.etr_ndir.place(relx=0.1, rely=0.18, relwidth=0.68, relheight=0.05)


    def change_new_entry_text(self, text):
        self.etr_ndir.delete(0, END)
        self.etr_ndir.insert(0, text)

    def change_origin_entry_text(self, text):
        self.etr_odir.delete(0, END)
        self.etr_odir.insert(0, text)

    def is_file_moved(self):
        self.lb_m = Label(self.root, text=f'Files moved')
        self.lb_m.place(relx = 0.45, rely = 0.9)

    def is_file_copied(self):
        self.lb_m = Label(self.root, text=f'Files copied')
        self.lb_m.place(relx = 0.45, rely = 0.9)


App()
