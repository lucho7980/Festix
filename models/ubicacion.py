import json
import uuid
class Ubicacion:
    def __init__ (self, nombre: str, direccion: str, longitud: float, latitud: float):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.direccion = direccion
        self.longitud  = longitud
        self.latitud = latitud
    
    def to_json(self):
        return { "nombre": self.nombre, "direccion": self.direccion, "longitud": self.longitud, "latitud": self.latitud}
    
    def guardar_en_json(self,archivo="data\\ubicacion.json"):
        """
        Guarda los datos de una ubicación en un archivo json
        """
        datos = self.to_json() # Crea un diccionario con los datos de la ubicacion
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json
    
    @classmethod    
    def from_json(cls, json_data):
        with open(json_data,"r") as f:
            data = json.loads(f)
        return [cls(**Ubicacion) for ubicacion in data]
        