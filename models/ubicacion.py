import json

class Ubicacion:
    def __init__ (self, id: int, nombre: str, direccion: str, coordenadas: list[float]):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas  = coordenadas
    
    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "direccion": self.direccion, "coordenadas": self.coordenadas}
    
    def guardar_en_json(self,archivo="data\\ubicacion.json"):
        """
        Guarda los datos de una ubicación en un archivo json
        """
        datos = self.to_json() # Crea un diccionario con los datos de la ubicacion
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json
    
    @classmethod    
    def from_json(cls, json_data="data\\ubicacion.json"):
        with open(json_data,"r") as f:
            data = json.loads(f)
        return cls(data["id"], data["nombre"], data["direccion"], data["coordenadas"])
        