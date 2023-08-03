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
        #RAIZ
        self.master = master
        self.controlador = controlador
        
        #self.title("FESTIX")
        #self.geometry("500x600")
        #self.columnconfigure(0, weight=1)
        #self.rowconfigure(0,weight=1)
        #self.resizable(False,False)
        
        #CONFIGURACION DE GRID LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #SCROLLBARFRAME
        self.titulo = ctk.CTkLabel(self,text="UBICACIONES",font=("Open Sans",30),text_color=blanco).pack(pady=30,padx=95)
        #LISTA DE UBICACIONES
        self.listbox = ctk.CTkScrollableFrame(self, width=200, height=200,border_color=rosa,scrollbar_button_color=rosa).pack(pady=25,padx=105)
        #BOTONES
        self.agregarUbi = ctk.CTkButton(
            self,
            text="AGREGAR UBICACIÓN",
            corner_radius=10,
            fg_color=cian).pack(pady=30,padx=90)
        self.boton_inicio = ctk.CTkButton(
            self,
            text="CERRAR SESIÓN",
            corner_radius=10,
            fg_color=rosa).pack(pady=10,padx=90)

    
"""   ESTRUCTURA LISTBOX PROPUESTA POR EL EJEMPLO DE BIBLIOTECA DE JUEGOS (TODAVÍA INCOMPATIBLE CON LA APP)
        #LISTA DE UBICACIONES
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        # Asocia el evento de doble clic a la función seleccionar_juego
        self.listbox.bind("<Double-Button-1>", self.seleccionar_ubicacion)

        self.listbox.pack(pady=25,padx=105)
        self.actualizar_ubicaciones()

        # Crea el botón para ir a inicio y lo agrega a la vista
        self.boton_inicio = ctk.CTkButton(
            self, text="Ir a Inicio", command=self.controlador.regresar_inicio,
            corner_radius=10,fg_color=cian
        )
        self.boton_inicio.pack(pady=10)  
""" 
""" DEFINICION DE FUNCIONES PROPUESTAS POR EL EJEMPLO DE BIBLIOTECA DE JUEGOS (TODAVÍA INCOMPATIBLE CON LA APP)
    def actualizar_ubicaciones(self):
        ubicaciones = self.controlador.obtener_ubicaciones()
        self.listbox.delete(0, tk.END)
        for juego in juegos:
            self.listbox.insert(tk.END, ubicacion.nombre)

    def obtener_ubicacion_seleccionada(self):
        indice = self.listbox.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_ubicacion(self, event):
        self.controlador.seleccionar_ubicacion()
 """   
 
     
if __name__ == "__main__":
    app = VistaUbicacion()
    app.mainloop()