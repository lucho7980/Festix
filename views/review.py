import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
#COLORES
blanco = "#eee"
gris = "#333333"
cian = "#00ffff"
rosa =  "#FF69B4"

class VistaReview(ctk.CTkFrame):
    def __init__(self,master=None,controlador=None):
        super().__init__(master)
        self.app = master
        self.controlador = controlador
        
        #CONFIGURACION DE GRID LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        #TITULO
        self.titulo = ctk.CTkLabel(self,text="REVIEWS",font=("Open Sans",30),text_color=blanco).pack(pady=20,padx=95)
        
        #LISTA REVIEWS
        self.scrollable = ctk.CTkScrollableFrame(self,corner_radius=15,scrollbar_button_color=gris,fg_color=gris,scrollbar_button_hover_color=gris,width=300)
        self.scrollable.pack(pady=10,padx=10)
        self.listbox = tk.Listbox(self.scrollable,background=gris,borderwidth=0,selectborderwidth=0)
        self.listbox.config(width=65,height=11)
        self.listbox.pack(pady=10,padx=10)
        
        #ENTRY
        self.review = ctk.CTkEntry(self,placeholder_text="Deje un comentario sobre el evento",border_color=cian,corner_radius=10,width=250)
        self.animo = ctk.CTkCheckBox(self)
        self.review.pack(pady=15,padx=10)
        
        #BOTON
        self.regresar = ctk.CTkButton(
            self,
            text="REGRESAR AL MAPA",
            corner_radius=10,
            fg_color=rosa,
            command=self.controlador.mostrar_mapa
            )
        self.regresar.pack(pady=0,padx=10)
        
        
        
        
if __name__ == "__main__":
    app= VistaReview()
    app.mainloop()