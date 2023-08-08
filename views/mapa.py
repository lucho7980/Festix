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
        self.titulo = ctk.CTkLabel(self,text="MAPA FESTIX",font=("Open Sans",30),text_color=blanco).pack(pady=20,padx=55)
        
        #WIDGET MAPA
        self.mapa = mapa.TkinterMapView(self,width=300, height=200,corner_radius=10)
        self.mapa.pack(pady=5,padx=10)
        
        #LABEL DE LA INFO DEL EVENTO
        self.ubicacion_label = tk.Label(self, text="",background=gris,fg=blanco)
        self.ubicacion_label.pack(pady=5)
        self.ubicacion_label.config(justify=tk.LEFT)
      
        #BOTONES
        ubicaciones = ctk.CTkButton(
            self,
            text="REGRESAR A UBICACIÓNES",
            corner_radius=10,
            fg_color=rosa,
            command=self.controlador.mostrar_ubicaciones
            ).pack(pady=10,padx=10)
        
    #MOSTRAR INFORMACION DE LA UBICACION
    def mostrar_info_ubicacion(self, ubicacion):
            info = f"Nombre: {ubicacion.nombre}\nDirección: {ubicacion.direccion}\nLongitud: {ubicacion.longitud}\nLatitud: {ubicacion.latitud}\nID: {ubicacion.id}"
            self.ubicacion_label["text"] = info
            
    #MUESTRA LA UBICACION EN EL MAPA Y PONE UNA MARCA
    def agregar_marcador(self,ubicacion):
        self.mapa.set_address(ubicacion.longitud,ubicacion.latitud)
        self.mapa.set_marker(ubicacion.longitud,ubicacion.latitud)
        
           
if __name__ == "__main__":
    app = VistaMapa()
    app.mainloop()