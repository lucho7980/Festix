import tkinter as tk
import customtkinter as ctk
import json as j

class MiApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("FESTIX")
        self.geometry("600x600")
        
class MiFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.crearWidgets()
        
        #Frame
        self.Frame = ctk.CTkFrame(self, width=600, height=600, bg="white")
        self.Frame.grid(row=0, column=0, sticky="nsew")
        self.Frame.grid_rowconfigure(0, weight=1)
        self.Frame.grid_columnconfigure(0, weight=1)
        #self.canvas.create_text(300, 50, text="FESTIX", font=("Arial", 32))
        #imagenHome = PhotoImage(file="assets\home.png")
        #self.Frame.create_image(0,0, image=imagenHome, anchor= tk.NW) 
        
        #Inicio Sesiom
        inicioSesiom = Label(self.Frame,text="INICIO DE SESION",bg="white")
        inicioSesiom.grid(row=0,column=2)
        
        #Entry Nombre
        nombre = Label(self.Frame,text="USUARIO:",bg="white")
        nombre.grid(row=2,column=1,pady=10,padx=5)
        self.EntryNombre = ctk.CTkEntry(self.Frame, width=235, height=20)
        self.EntryNombre.grid(row=2,column=2)
        
        #Entry password
        contrasenia = Label(self.Frame,text="CONTRASEÑA:",bg="white")
        contrasenia.grid(row=3,column=1,pady=10,padx=5)
        self.EntryContra = ctk.CTkEntry(self.Frame, width=235, height=20)
        self.EntryContra.grid(row=3,column=2)
        
        #Botones
        self.boton_enviar = ctk.CTkButton(self.Frame, text="ENVIAR", command=self.saludar)
        self.boton_enviar.grid(row=4,column=2)
        
    """   
    def cambiarGUI():
        pass
    
    def IniciarSesion(self,archivo="data\inicio_sesion.inicio_sesion.json"):
        user = self.EntryNombre.get()
        passw = self.EntryContra.get()
        with open(archivo,"r") as file:
            if file[usuario] == user and file[contrasenia] == passw:
                cambiarGUI()
            else:
                return "El usuario o la contraseña no coinciden con algún usuario registrado."
            
    def registrarCuenta(self,archivo="data\inicio_sesion.inicio_sesion.json"):
        user = self.EntryNombre.get()
        passw = self.EntryContra.get()
        with open(archivo,"w") as file:
            file[usuario] = user
            file[contrasenia] = passw
    """        
        
        
if __name__ == "__main__":
 app = MiApp()
 frame = MiFrame(master=app)
 frame.grid(sticky="nsew") 
 app.mainloop()

