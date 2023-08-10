import json
import uuid
class Usuario:
    def __init__ (self, nombre: str, contrasenia: str):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.contrasenia = contrasenia
        self.historial_eventos = []
    
    @classmethod    
    def cargar_datos(cls):
        with open("data/inicio_sesion.json", "r") as json_file:
            return json.load(json_file)
    
    #VERIFICA SI EL USUARIO YA EXISTE
    @classmethod
    def autenticar(cls, nombre, contrasenia):
        datos = cls.cargar_datos()
        for data in datos:
            if nombre == data["usuario"] and contrasenia == data["contrasenia"]:
                return True
        return False
    
    #REGISTRA EL USUARIO
    @classmethod
    def registrar(cls, nombre, contrasenia):
        datos = cls.cargar_datos()
        
        for data in datos:
            if nombre == data["usuario"]:
                return False

        nuevo_usuario = {"id": str(uuid.uuid4()), "usuario": nombre, "contrasenia": contrasenia, "historial_eventos": []}
        datos.append(nuevo_usuario)
        
        with open("data/inicio_sesion.json", "w") as json_file:
            json.dump(datos, json_file, indent=4)

        return True
    
    
    def agregar_al_historial(self,id):
        """
        Agrega un evento al historial de eventos del usuario a través de un ID (Eventos a los que ya ha asisitido)
        """
        if isinstance(id,int): #El id debe ser estríctamente int
            self.historial_eventos.append(id)
        else:
            print("Código erróneo")

#    def to_json(self):
#        return {"id": self.id, "nombre": self.nombre, "apellido": self.apellido, "historial_eventos": self.historial_eventos}
#   
#    def guardar_en_json(self,archivo="data\\usuario.json"):
#        """
#        Guarda los datos del usuario en un archivo json
#        """
#        datos = self.to_json()
#        with open(archivo,"w") as file: # Abrir el archivo en modo escritura
#            json.dump(datos,file) # Guardar el diccionario en formato json
    

#    @classmethod    
#    def from_json(cls, json_data="data\\usuario.json"):
#        with open(json_data,"r") as f:
#            data = json.loads(f)
#        return cls(data["id"], data["nombre"], data["apellido"], data["historial_eventos"])
    
    
    