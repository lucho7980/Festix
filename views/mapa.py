import tkinter as tk
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
        self.mapa.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
        self.mapa.pack(pady=5,padx=10)
        
        #LABEL DE LA INFO DEL EVENTO
        self.ubicacion_label = tk.Label(self, text="",background=gris,fg=blanco)
        self.ubicacion_label.pack(pady=5)
        self.ubicacion_label.config(justify=tk.LEFT)
      
        #BOTONES
        self.ubicaciones = ctk.CTkButton(
            self,
            text="REGRESAR A UBICACIONES",
            corner_radius=10,
            fg_color=rosa,
            command=self.controlador.mostrar_ubicaciones
            )
        self.ubicaciones.pack(pady=10,padx=10)
        
        self.reviews = ctk.CTkButton(
            self,
            text="AGREGAR UNA REVIEW",
            corner_radius=10,
            fg_color=cian,
            command=self.controlador.mostrar_ubicaciones
            )
        self.reviews.pack(pady=10,padx=10)
        
    #MOSTRAR INFORMACION DE LA UBICACION
    def mostrar_info_ubicacion(self, ubicacion):
            info = f"Nombre: {ubicacion.nombre}\nDirección: {ubicacion.direccion}"
            self.ubicacion_label["text"] = info
            
    #MUESTRA LA UBICACION EN EL MAPA Y PONE UNA MARCA
    def agregar_marcador(self,ubicacion):
        self.mapa.set_position(ubicacion.latitud, ubicacion.longitud)
        self.mapa.set_marker(ubicacion.latitud, ubicacion.longitud)
        
           
if __name__ == "__main__":
    app = VistaMapa()
    app.mainloop()