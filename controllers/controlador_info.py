class ControladorInfo:
    def __init__(self,app):
       self.app = app
        
    def mostrar_ubicaciones(self):
        self.app.cambiar_frame(self.app.vista_ubicaciones)
    
    def mostrar_review(self) :
        self.app.cambiar_frame(self.app.vista_review)
        