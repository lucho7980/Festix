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

class VistaMapa(ctk.CTkFrame):
    def __init__(self,master=None,controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="MAPA FESTIX",font=("Open Sans",30),text_color=blanco).pack(pady=30,padx=55)
        
        #WIDGET MAPA
        self.mapa = mapa.TkinterMapView(self,width=300, height=200,corner_radius=10)
        self.mapa.pack(pady=10,padx=10)
        self.mapa.set_address("Salta, Salta,Argentina",marker=True)
        
        #LABEL DE LA INFO DEL EVENTO
        self.ubicacion_label = tk.Label(self, text="")
        self.ubicacion_label.pack(pady=50)
        self.ubicacion_label.config(justify=tk.LEFT)
        #MOSTRAR INFORMACION DE LA UBICACION
        def mostrar_info_ubicacion(self, ubicacion):
            info = f"Nombre: {ubicacion.nombre}\nDirección: {ubicacion.direccion}\nCoordenadas: {ubicacion.coordenadas}\nID: {ubicacion.id}"
            self.ubicacion_label["text"] = info
        
        
        #BOTONES
        ubicaciones = ctk.CTkButton(
            self,
            text="REGRESAR A UBICACIÓNES",
            corner_radius=10,
            fg_color=rosa,
            command=self.controlador.mostrar_ubicaciones
            ).pack(pady=5,padx=10)
           
if __name__ == "__main__":
    app = VistaMapa()
    app.mainloop()