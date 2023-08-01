import json

class rutaVisita:
    def __init__ (self, id: int, nombre: str, destinos: list[int]):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "destinos": self.destinos}
    
    def guardar_en_json(self,archivo="data\ruta_visitada.json"):
        """
        Guarda los datos del destino en un archivo json
        """
        datos = self.to_json() # Crea un diccionario con los datos del destino
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json

    @classmethod    
    def from_json(cls, json_data="data\ruta_visitada.json"):
        with open(json_data,"r") as f:
            data = json.loads(f)
        return cls(data["id"], data["nombre"], data["destinos"])
