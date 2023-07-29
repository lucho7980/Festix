import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
#COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa =  "#FF69B4"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #RAIZ
        self.title("FESTIX")
        self.geometry("500x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)
        self.resizable(False,False)
        #CONFIGURACION DE GRID LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        #SCROLLBARFRAME
        self.titulo = ctk.CTkLabel(self,text="UBICACIONES",font=("Open Sans",30),text_color=blanco).pack(pady=30,padx=95)
          #LISTA DE UBICACIONES
        self.listbox = ctk.CTkScrollableFrame(self, width=200, height=200,border_color=rosa,scrollbar_button_color=rosa).pack(pady=25,padx=105)
        #BOTONES
        self.agregarUbi = ctk.CTkButton(self,text="AGREGAR UBICACIÓN",corner_radius=10,fg_color=cian).pack(pady=30,padx=90)
                
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()