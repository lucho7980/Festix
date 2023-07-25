import tkinter as tk
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("FESTIX")
        self.geometry("600x600")
        
class MiFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.crearWidgets()
    
    def crearWidgets(self):
        #Frame
        self.Frame = tk.Frame(self, width=600, height=600, bg="white")
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
    
    def saludar(self):
        """
        nombre = self.EntryNombre.get() 
        mensaje = f"¡Bienvenido, {nombre}!"
        self.EntryNombre.delete(0,tk.END)
        self.EntryNombre.insert(0,mensaje)
        """
        mensaje = self.EntryNombre.get()
        return messagebox.showinfo("¡Bienvenido¡",mensaje)
        
        
if __name__ == "__main__":
 app = MiApp()
 frame = MiFrame(master=app)
 frame.grid(sticky="nsew") 
 app.mainloop()

