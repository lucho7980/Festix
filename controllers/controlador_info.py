class ControladorInfo:
    def __init__(self,app):
       self.app = app
        
    def regresar_ubicaciones(self):
        self.app.cambiar_frame(self.app.vista_ubicaciones)