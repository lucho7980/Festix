import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark") 
#COLORES
blanco = "#eee"
gris = "#444444"
cian = "#00ffff"
rosa =  "#FF69B4"

class VistaInfo(ctk.CTkFrame):
    def __init__(self,master=None,controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        
        #CONFIGURACION DE GRID LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="INFORMACION DE LA UBICACIÓN",font=("Open Sans",30),text_color=blanco).pack(pady=40,padx=10)
        self.ubicaciom_label = ctk.CTkLabel(self, text="")
        self.ubicaciom_label.pack(pady=50)
        self.ubicaciom_label.configure(justify=tk.LEFT)
        self.boton_regresar = ctk.CTkButton(
            self,
            text="Regresar a la lista de Ubicaciones",
            corner_radius=10,
            fg_color=rosa,
           # command=self.controlador.regresar_ubicaciones
            )
        self.boton_regresar.pack(pady=10)
        
app= VistaInfo()
app.mainloop()