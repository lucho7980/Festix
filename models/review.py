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
        
    @classmethod    
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["id"], data["id_evento"], data["id_usuaro"], data["calificacion"], data["comentario"], data["animo"])
    