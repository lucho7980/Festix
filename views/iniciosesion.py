import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
#COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa =  "#FF69B4"

class VistaInicio(ctk.CTkFrame):
    def __init__(self,master=None,controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="BIENVENIDO",font=("Open Sans",30),text_color=blanco).pack(pady=25,padx=10)
        
        self.linea1 = ctk.CTkLabel(self,text="___________",font=("Open Sans",30),text_color=rosa).pack(pady=15,padx=10)

        #ENTRYS
        self.nombre = ctk.CTkEntry(self,placeholder_text="Nombre...",border_color=cian,corner_radius=10)
        self.nombre.pack(pady=10,padx=10)
        self.password = ctk.CTkEntry(self,placeholder_text="Contraseña...",border_color=rosa,show="*",corner_radius=10)
        self.password.pack(pady=10,padx=10)
        
        #BOTONES
        def IniciarSesion(self):
            pass
        def registrarCuenta(self,label):
            pass
       
        self.enviar = ctk.CTkButton(self,text="ENVIAR",corner_radius=10,fg_color=cian,command=self.controlador.mostrar_ubicaciones).pack(pady=10,padx=10)
        self.registrar = ctk.CTkButton(self,text="REGISTRARSE",corner_radius=10,fg_color=rosa,command=self.controlador.mostrar_ubicaciones).pack(pady=10,padx=10)
        
        self.linea2 = ctk.CTkLabel(self,text="___________",font=("Open Sans",30),text_color=cian).pack(pady=15,padx=10)
        
if __name__ == "__main__":
    app = VistaInicio()
    app.mainloop()