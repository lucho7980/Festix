import tkinter as tk
import tkintermapview as mapa
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
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="MAPA FESTIX",font=("Open Sans",30),text_color=blanco).pack(pady=30,padx=95)
        
        #WIDGET MAPA
        self.mapa = mapa.TkinterMapView(self,width=600, height=400)
        self.mapa.pack(pady=10,padx=10)
        self.mapa.set_position(48.8584, 2.2945) #PARIS
        
if __name__ == "__main__":
    app = App()
    app.mainloop()