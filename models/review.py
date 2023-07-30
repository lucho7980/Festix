import json

class Review:
    def __init__ (self, id: int, id_evento: int, id_usuario: int, calificacion: int, comentario: str, animo: str):
        """
        calificacion int 1 to 5
        animo str "Positivo" o "Negativo"
        """
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        return {"id": self.id, "id_evento": self.id_evento, "id_usuario": self.id_usuario, "calificacion": self.calificacion, "comentario": self.comentario, "animo": self.animo}
    
    def guardar_en_json(self,archivo="data\review.json"):
        """
        Guarda los datos de la review en un archivo json
        """
        datos = to_json() # Crea un diccionario con los datos de la review
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json
        
    @classmethod    
    def from_json(cls, json_data="data\review.json"):
        with open(json_data,"r") as f:
            data = json.loads(f)
        return cls(data["id"], data["id_evento"], data["id_usuaro"], data["calificacion"], data["comentario"], data["animo"])
    