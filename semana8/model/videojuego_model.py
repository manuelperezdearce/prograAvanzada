from model.database import Database

class VideojuegoModel:
    
    def __init__(self):
        self.db = Database()
    
    def readAll(self):
        data = self.db.query("SELECT * FROM videojuego")
        return data
    def insert(self, titulo, genero, clasificacion, plataforma):
        print("Vamos a guardar estamos en el modelo")
        sql = "INSERT INTO videojuego (titulo, genero, clasificacion, plataforma) VALUES (%s, %s, %s, %s)"
        return self.db.execute(sql, (titulo, genero, clasificacion, plataforma))