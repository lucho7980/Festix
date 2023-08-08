import tkinter as tk
import customtkinter as ctk
from models.usuario import Usuario
from models.ubicacion import Ubicacion
from models.evento import Evento
from views.iniciosesion import VistaInicio
from views.ubicacion import VistaUbicacion
from views.mapa import VistaMapa
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_ubicacion import ControladorUbicacion
from controllers.controlador_info import ControladorInfo

class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FESTIX")
        self.geometry("394x500")
        self.resizable(False,False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.config(bg="#222222",pady=30)
        
    def inicializar(self):
        ubicaciones = Ubicacion.from_json("data/ubicacion.json")
        
        controlador_inicio = ControladorInicio(self)
        controlador_ubicacion = ControladorUbicacion(self,ubicaciones)
        controlador_info = ControladorInfo(self)
        
        self.vista_inicio = VistaInicio(self,controlador_inicio)
        self.vista_ubicaciones = VistaUbicacion(self,controlador_ubicacion)
        self.vista_mapa = VistaMapa(self, controlador_info)
        
        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_ubicaciones)
        self.ajustar_frame(self.vista_mapa)
        
    def ajustar_frame(self,frame):
        frame.grid(row=0,column=0,sticky="nsew")
    
    def cambiar_frame(self,frame_destino):
        frame_destino.tkraise()
        
        
if __name__ == "__main__":
    app= Aplicacion()
    app.mainloop()