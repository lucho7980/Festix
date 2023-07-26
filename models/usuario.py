import json

class Usuario:
    def __init__ (self, id: int, nombre: str, apellido: str, historial_eventos: list[int]):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        if historial is none:
            self.historial_eventos = []
        else:
            self.historial_eventos = historial_eventos
        
    def agregar_al_historial(self,id):
        """
        Agrega un evento al historial de eventos del usuario a través de un ID (Eventos a los que ya ha asisitido)
        """
        if isinstance(id,int): #El id debe ser estríctamente int
            self.historial_eventos.append(id)
        else:
            print("Código erróneo")

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "apellido": self.apellido, "historial_eventos": self.historial_eventos}
   
    def guardar_en_json(self,archivo="data\\usuario.json"):
        """
        Guarda los datos del usuario en un archivo json
        """
        datos = to_json()
        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
            json.dump(datos,file) # Guardar el diccionario en formato json
    

    @classmethod    
    def from_json(cls, json_data="data\\usuario.json"):
        data = json.loads(json_data)
        return cls(data["id"], data["nombre"], data["apellido"], data["historiaL_eventos"])
    
    
    