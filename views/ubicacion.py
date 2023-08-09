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
        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)
        
        # Asocia el evento de doble clic a la función seleccionar_juego
        self.listbox.bind("<Double-Button-1>", self.seleccionar_ubicacion)

        self.listbox.pack(pady=10)
        
        self.actualizar_ubicaciones()
        self.obtener_ubicacion_seleccionada()
        
        self.linea = ctk.CTkLabel(self,text="___________",font=("Open Sans",30),text_color=rosa).pack(pady=15,padx=10)
        
        #BOTONES
        self.boton_inicio = ctk.CTkButton(
            self,
            text="CERRAR SESIÓN",command= self.controlador.mostrar_inicio,
            corner_radius=10,
            fg_color=cian).pack(pady=30,padx=90)      
        
           #FUNCIONES 
    def actualizar_ubicaciones(self):
            ubicaciones = self.controlador.return_ubicaciones()
            self.listbox.delete(0, tk.END)
            for ubicacion in ubicaciones:
                self.listbox.insert(tk.END, ubicacion.nombre)


    def obtener_ubicacion_seleccionada(self):
            indice = self.listbox.curselection()
            if indice:
                return indice[0]
            else:
                return None

    def seleccionar_ubicacion(self, event):
            self.controlador.seleccionar_ubicacion()
        
              
        
if __name__ == "__main__":
    app = VistaUbicacion()
    app.mainloop()