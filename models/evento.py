import datetime
import json

class Evento:
    def __init__ (self, id: int, nombre: str, artista: str, genero: str, id_ubicacion: int, hora_inicio: str, hora_fin: str, descripcion: str, imagen: str):
        """
        hora_inicio datetime ISO 8601
        """
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = datetime.fromisoformat(hora_inicio)
        self.hora_fin = datetime.fromisoformat(hora_fin)
        self.descripcion = descripcion
        self.imagen = imagen

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "artista": self.artista, "genero": self.genero, "id_ubicacion": self.id_ubicacion,
                "hora_inicio": self.hora_inicio.isoformat() , "hora_fin": self.hora_fin.isoformat(),
                "descripcion": self.descripcion, "imagen": self.imagen}
    
    def guardar_en_json(self,archivo="data\evento.json"):
        """
        Guarda los datos del usuario en un archivo json
        """
        datos = self.to_json()# Crea un diccionario con los datos del usuario
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json 
    
    @classmethod    
    def from_json(cls, json_data="data\evento.json"):
        with open(json_data,"r") as f:
            data = json.loads(f)
        return cls(data["id"], data["nombre"], data["artista"], data["genero"], data["id_ubicacion"],
                   datetime.fromisoformat(data["hora_inicio"]), datetime.fromisoformat(data["hora_fin"]),
                   data["descripcion"], data["imagen"])
    
