import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
#COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa =  "#FF69B4"

class VistaUbicacion(ctk.CTkFrame):
    def __init__(self,master=None,controlador=None):
        super().__init__(master)
        self.app = master
        self.controlador = controlador
        
        #CONFIGURACION DE GRID LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="UBICACIONES",font=("Open Sans",30),text_color=blanco).pack(pady=30,padx=95)
        
        #LISTA DE UBICACIONES
        self.scrollableframe = ctk.CTkScrollableFrame(self, width=200, height=200, border_color=rosa, scrollbar_button_color=rosa)
        self.scrollableframe.pack(pady=0, padx=105)

        self.boton_ubicacion1 = ctk.CTkButton(self.scrollableframe, text="", corner_radius=10, fg_color=cian,command=self.controlador.mostrar_mapa)
        self.boton_ubicacion1.pack(pady=10)

        self.boton_ubicacion2 = ctk.CTkButton(self.scrollableframe, text="", corner_radius=10, fg_color=cian,command=self.controlador.mostrar_mapa)
        self.boton_ubicacion2.pack(pady=10)

        self.boton_ubicacion3 = ctk.CTkButton(self.scrollableframe, text="", corner_radius=10, fg_color=cian,command=self.controlador.mostrar_mapa)
        self.boton_ubicacion3.pack(pady=10)

        self.boton_ubicacion4 = ctk.CTkButton(self.scrollableframe, text="", corner_radius=10, fg_color=cian,command=self.controlador.mostrar_mapa)
        self.boton_ubicacion4.pack(pady=10)

        #BOTONES
        self.boton_inicio = ctk.CTkButton(
            self,
            text="CERRAR SESIÓN",command= self.controlador.mostrar_inicio,
            corner_radius=10,
            fg_color=cian).pack(pady=30,padx=90)
       
        
     
if __name__ == "__main__":
    app = VistaUbicacion()
    app.mainloop()