from tkinter import messagebox
import customtkinter as ctk
from models.usuario import Usuario

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
        
        #FUNCIONES DE INICIO DE SESION Y REGISTRO
        
        def IniciarSesion():
            
            usuario = self.nombre.get()
            password = self.password.get()

            
            if Usuario.autenticar(usuario, password):
                self.controlador.mostrar_ubicaciones()
                return
            messagebox.showerror("Error","El usuario o la contraseña no son correctos, reintente.")
        
        def registrarse():
            usuario = self.nombre.get()
            password = self.password.get()
            
            if Usuario.registrar(usuario, password):
                messagebox.showinfo("Usuario", "Se registro con exito.")
            else:
                messagebox.showinfo("Atencion", "El usuario ya existe.")
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="BIENVENIDO",font=("Open Sans",30),text_color=blanco).pack(pady=25,padx=10)
        
        self.linea1 = ctk.CTkLabel(self,text="___________",font=("Open Sans",30),text_color=rosa).pack(pady=15,padx=10)

        #ENTRYS
        self.nombre = ctk.CTkEntry(self,placeholder_text="Usuario",border_color=cian,corner_radius=10)
        self.nombre.pack(pady=10,padx=10)
        self.password = ctk.CTkEntry(self,placeholder_text="Contraseña",border_color=rosa,corner_radius=10)
        self.password.configure(show="*")
        self.password.pack(pady=10,padx=10)
        
        #BOTONES
        self.enviar = ctk.CTkButton(self,text="INICIAR SESION",corner_radius=10,fg_color=cian,command= IniciarSesion).pack(pady=10,padx=10)
        self.registrar = ctk.CTkButton(self,text="REGISTRARSE",corner_radius=10,fg_color=rosa, command= registrarse).pack(pady=10,padx=10)
        
        self.linea2 = ctk.CTkLabel(self,text="___________",font=("Open Sans",30),text_color=cian).pack(pady=5,padx=10)
        
if __name__ == "__main__":
    app = VistaInicio()
    app.mainloop()