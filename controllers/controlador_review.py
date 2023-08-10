class ControladorReview:
    def __init__(self,app):
        self.app = app
    
    def mostrar_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)