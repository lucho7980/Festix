import tkinter as tk
from tkintermapview import TkinterMapView
import tkintermapview as mapa
import customtkinter as ctk


ctk.set_appearance_mode("dark") 
#COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa =  "#FF69B4"

class VistaMapa(ctk.CTk):
    def __init__(self,master=None,controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.ubicaciones = []
        
        #RAIZ
        self.title("FESTIX")
        self.geometry("500x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)
        self.resizable(False,False)
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="MAPA FESTIX",font=("Open Sans",30),text_color=blanco).pack(pady=30,padx=95)
        
        #WIDGET MAPA
        self.mapa = mapa.TkinterMapView(self,width=600, height=400,corner_radius=10)
        self.mapa.pack(pady=10,padx=10)
        self.mapa.set_address("Salta,Salta,Argentina",marker=True) #PARIS
        
        #BOTONES
        ubicaciones = ctk.CTkButton(
            self,
            text="REGRESAR A UBICACIÓNES",
            corner_radius=10,
            fg_color=rosa,
           # command=self.controlador.regresar_ubicaciones
            ).pack(pady=5,padx=10)
        add = ctk.CTkButton(
            self,
            text="AÑADIR UBICACIÓN",
            corner_radius=10,
            fg_color=cian,
           # command=self.controlador.regresar_ubicaciones
            ).pack(pady=5,padx=10)
        
        
        def Añadir_marcador_de_evento(cords):
            """
            Recibe las coordenadas proporcionadas por add_left_click_map_command y las agrega al mapa.
            Además crea una tupla con los datos de la ubicación agregada en una lista.
            """
            lista = []
            nombre = input("Nombre de la ubicación: ")
            click = self.mapa.set_marker(cords[0], cords[1], text=nombre)
            direccion = (cords[0],cords[1])
            lista.append((nombre,direccion,[cords[0], cords[1]]))
            mensaje = tk.messagebox.showinfo("Eventos",f"'{nombre}' se agregó con éxito")
           
            return lista

        self.ubicaciones = self.mapa.add_left_click_map_command(Añadir_marcador_de_evento)

if __name__ == "__main__":
    app = VistaMapa()
    app.mainloop()