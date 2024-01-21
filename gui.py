from tkinter import *
from tkinter import filedialog
from tkinter import ttk
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
 
    def open_origin_folder(self):
        self.etr_odir = filedialog.askdirectory()
    def open_new_folder(self):
        self.etr_ndir = filedialog.askdirectory()

    def copy_files(self):
        move_copy.Mc_file(self.etr_odir, self.etr_ndir).copy()
    def move_files(self):
        move_copy.Mc_file(self.etr_odir, self.etr_ndir).move()


    def origin_new_dir(self):
        # Select Origin directory btn
        self.btn_odir = Button(self.root, text='Origin Directory', command=self.open_origin_folder)
        self.btn_odir.place(relx=0.8, rely=0.1, relwidth=0.15, relheight=0.05)

        # Select New Directory btn
        self.btn_ndir = Button(self.root, text='New Directory', command=self.open_new_folder)
        self.btn_ndir.place(relx=0.8, rely=0.18, relwidth=0.15, relheight=0.05)

        # Copy btn
        self.copy_btn = Button(self.root, text='Copy files', command=self.copy_files)
        self.copy_btn.place(relx= 0.3, rely = 0.9, relwidth=0.15, relheight=0.05)

        # Move btn
        self.move_btn = Button(self.root, text='Move files', command=self.move_files)
        self.move_btn.place(relx=0.6, rely=0.9, relwidth=0.15, relheight=0.05)

        # Origin directory Entry
        self.etr_odir = Entry(self.root)
        self.etr_odir.place(relx=0.1, rely=0.1, relwidth=0.68, relheight=0.05)

        # New Directory Entry
        self.etr_ndir = Entry(self.root)
        self.etr_ndir.place(relx=0.1, rely=0.18, relwidth=0.68, relheight=0.05)


        #tree view
        self.list_files = ttk.Treeview(self.root, height=3, columns=("col1", "col2"))
        self.list_files.heading("#0", text="")
        self.list_files.heading("#1", text="file_name")
        self.list_files.heading("#2", text="extension")
        
        self.list_files.column("#0", width=1)
        self.list_files.column("#1", width=200)
        self.list_files.column("#2", width=10)

        self.list_files.place(relx= 0.1, rely = 0.25, relwidth=0.85, relheight=0.5)




    

App()
