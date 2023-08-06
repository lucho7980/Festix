

class ControladorUbicacion:
    def __init__(self,app,modelo_ubicaciones):
        self.app = app
        self.modelo_ubicaciones = modelo_ubicaciones
        
    def obtener_ubicaciones(self):
        return self.modelo_ubicaciones
    
    def seleccionar_ubicacion(self):
        indice = self.app.vista_ubicaciones.obtener_ubicacion_seleccionada()
        if indice is not None:
            ubicacion = self.modelo_ubicaciones[indice]
            self.app.vista_info.mostrar_info_ubicacion(ubicacion)    
            self.app.cambiar_frame(self.app.vista_info)
            
    def mostrar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
        
    def mostrar_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)    
        
        