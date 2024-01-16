from tkinter import *
import move_copy

root = Tk()
path = move_copy.Mc_file(r'C:\Users\hevan\Desktop\Mc_test\or', r'C:\Users\hevan\Desktop\Mc_test\ds')
class App():
    def __init__(self):
        self.root = root
        self.window()
        root.mainloop()
    def window(self):
        self.root.title('Copiar ou Mover arquivos')
        self.root.geometry('720x600')
        self.root.resizable(False, False)
    
App()