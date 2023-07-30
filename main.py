import tkinter as tk
import customtkinter as ctk
from models.usuario import Usuario
from models.ubicacion import Ubicacion
from models.evento import Evento
from views.iniciosesion import VistaInicio
from views.ubicacion import VistaUbicacion
from views.mapa import VistaMapa
from controllers.inicio import ControladorInicio
from controllers.usuario import ControladorUsuario
from controllers.ubicacion import ControladorUbicacion
from controllers.evento import ControladorEvento

class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__(self)
        self.title("FESTIX")
        self.geometry("400x500")
        self.resizable(False,False)
        self.inicializar()
        self.cambiar_frame(self,Inicio_sesion)
        
    def inicializar(self):
        ubicaciones = Ubicacion.from_json("data/ubicacion.json")
        
        controlador_inicio = ControladorInicio(self)
        controlador_ubicaciones = ControladorUbicacion(self)
        controlador_evento = ControladorEvento(self)
        
        self.vista_inicio = VistaInicio(self,controlador_inicio)
        self.vista_ubicaciones = VistaUbicacion(self, controlador_ubicaciones)
        self.vista_mapa = VistaMapa(self, controlador_evento)
        
        self.ajustar_frame(self,vista_inicio)
        self.ajustar_frame(self,vista_ubicaciones)
        self.ajustar_frame(self,vista_mapa)
        
    def ajustar_frame(self,frame):
        frame.grid(row=0,column=0,sticky="nsew")
    
    def cambiar_frame(self,frame_destino):
        frame_destino.tkraise()
        
        
if __name__ == "__main__":
    app= Aplicacion()
    app.mainloop()