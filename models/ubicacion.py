import json

class Ubicacion:
    def __init__ (self, id, nombre: str, direccion: str, latitud: float, longitud: float):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.longitud  = longitud
        self.latitud = latitud
    
    def to_json(self):
        return {"id":self.id, "nombre": self.nombre, "direccion": self.direccion,"latitud": self.latitud, "longitud": self.longitud}
    
    def guardar_en_json(self,archivo):
        """
        Guarda los datos de una ubicación en un archivo json
        """
        datos = self.to_json() # Crea un diccionario con los datos de la ubicacion
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json       
            
    @classmethod    
    def from_json(cls, json_data):
        with open(json_data, "r") as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]


        