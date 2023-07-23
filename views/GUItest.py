import tkinter as tk

raiz = tk.Tk()
raiz.title("FESTIX")
frame =  tk.Frame(raiz).pack

#BOTONES
def saludar():
    return "Hola"

botonInicio = tk.Button(frame, text="ENVIAR",command=saludar).pack()


raiz.mainloop()