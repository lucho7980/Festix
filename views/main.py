import customtkinter as ctk
import tkinter as tk

#COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa =  "#FF69B4"

#RAIZ
root= ctk.CTk()
root.title("FESTIX")
root.geometry("500x600")
root.config(bg=blanco)
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)
root.resizable(False,False)

#FRAME
frame = ctk.CTkFrame(root,fg_color=gris)
frame.grid(column=0,row=0, sticky="nsew",pady=50,padx=50)

#LOGO 
"""
img = tk.PhotoImage(file="assets/logob.png")
img1 = img.subsample(4,4)
imagen = tk.Label(frame,image=img1).grid(row=0,column=2,pady=30)
#root.call("wm","iconphoto",root._w,logo)
"""

#TITULO
titulo = ctk.CTkLabel(frame,text="BIENVENIDO",font=("Open Sans",30),text_color=blanco).grid(row=1,column=2,pady=45)
linea1 = ctk.CTkLabel(frame,text="___________",font=("Open Sans",30),text_color=rosa).grid(row=2,column=2)
linea2 = ctk.CTkLabel(frame,text="___________",font=("Open Sans",30),text_color=cian).grid(row=7,column=2)

#ENTRYS

nombre = ctk.CTkEntry(frame,placeholder_text="Nombre...",border_color=cian,fg_color=blanco,corner_radius=10)
nombre.grid(row=3,column=2,pady=20,padx=130)
password = ctk.CTkEntry(frame,placeholder_text="Contraseña...",border_color=rosa,show="*",corner_radius=10)
password.grid(row=4,column=2)

#BOTON

def IniciarSesion(self):
        pass
        
def registrarCuenta(self):
        pass


enviar = ctk.CTkButton(frame,text="ENVIAR",corner_radius=10,fg_color=cian,command=IniciarSesion("data\inicio_sesion.json")).grid(row=5,column=2,pady=30)
registrar = ctk.CTkButton(frame,text="REGISTRARSE",corner_radius=10,fg_color=rosa,command=registrarCuenta("data\inicio_sesion.json")).grid(row=6,column=2)






root.mainloop()