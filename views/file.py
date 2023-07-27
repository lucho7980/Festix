import customtkinter as ctk
import tkinter

ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("FESTIX")
        self.geometry("500x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.config(bg="#444")
        imagen= tkinter.PhotoImage(file="assets/home.png")
        self.call("wm","iconphoto",self._w,imagen)
        ctk.set_default_color_theme("dark-blue")
       
        
class Frame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.crearWidgets()
        
    def crearWidgets(self):
        entry = ctk.CTkEntry(self,placeholder_text="Nombre...")

app = App()
app.mainloop()