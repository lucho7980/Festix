import json
import uuid
class Review:
    def __init__ (self, id_evento: int, id_usuario: int, calificacion: int, comentario: str, animo: str):
        """
        calificacion int 1 to 5
        animo str "Positivo" o "Negativo"
        """
        self.id = str(uuid.uuid4())
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        return {"id": self.id, "id_evento": self.id_evento, "id_usuario": self.id_usuario, "calificacion": self.calificacion, "comentario": self.comentario, "animo": self.animo}
    
    def guardar_en_json(self,archivo="data/review.json"):
        """
        Guarda los datos de la review en un archivo json
        """
        datos = self.to_json() # Crea un diccionario con los datos de la review
        with open(archivo,"a") as file: # Abre el archivo en modo append, asi se agrega cada review en el json
            json.dump(datos,file) # Guardar el diccionario en formato json
        
    @classmethod    
    def from_json(cls, json_data="data/review.json"):
        pass
    
    
    @classmethod
    def mostrar_comentarios(cls, reviews):
        for review in reviews:
            print(f"Calificación: {review.calificacion}")
            print(f"Comentario: {review.comentario}")
            print(f"Animo: {review.animo}")
            print("------------------------")

# Ejemplo de uso:

# Crear una nueva review y guardarla en el archivo json
#review1 = Review(123, 456, 5, "Excelente evento", "Positivo")
#review1.guardar_en_json()

#review2 = Review(124, 457, 4, "Buen evento", "Positivo")
#review2.guardar_en_json()

#review3 = Review(125, 458, 3, "Regular evento", "Negativo")
#review3.guardar_en_json()
# Cargar las reviews desde el archivo
#reviews = Review.from_json()

# Mostrar los comentarios y calificaciones
#Review.mostrar_comentarios(reviews)