import json

class rutaVisita:
    def __init__ (self, id: int, nombre: str, destinos: list[int]):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "destinos": self.destinos}
    
    def guardar_en_json(self,archivo):
        """
        Guarda los datos del destino en un archivo json
        """
        datos = to_json() # Crea un diccionario con los datos del destino
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json

    @classmethod    
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["id"], data["nombre"], data["destinos"])
