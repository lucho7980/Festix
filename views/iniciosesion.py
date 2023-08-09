from tkinter import messagebox
import customtkinter as ctk
import json


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
        
        def IniciarSesion():
            with open("data/inicio_sesion.json", "r") as json_file:
                datos = json.load(json_file)
            
            usuario = self.nombre.get()
            password = self.password.get()

            for data in datos:
                if usuario == data["usuario"] and password == data["contrasenia"]:
                    self.controlador.mostrar_ubicaciones()
                    return
            messagebox.showerror("Error","El usuario o la contraseña no son correctos, reintente.")
        
        def registrarse():
            usuario = self.nombre.get()
            password = self.password.get()

            with open("data/inicio_sesion.json", "r") as json_file:
                datos = json.load(json_file)
            for data in datos:
                if usuario == data["usuario"]:
                    messagebox.showinfo("Atencion", "El usuario ya existe.")
                    return
            
            nuevo_usuario = {"usuario": usuario, "contrasenia": password}
            datos.append(nuevo_usuario)
            with open("data/inicio_sesion.json", "w") as json_file:
                json.dump(datos, json_file, indent=4)
                
            messagebox.showinfo("Usuario", "Se registro con exito.")

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
        self.registrar = ctk.CTkButton(self,text="REGISTRARSE",corner_radius=10,fg_color=rosa,command= registrarse).pack(pady=10,padx=10)
        
        self.linea2 = ctk.CTkLabel(self,text="___________",font=("Open Sans",30),text_color=cian).pack(pady=15,padx=10)
        
if __name__ == "__main__":
    app = VistaInicio()
    app.mainloop()