from model.database import Database

class VideojuegoModel:
    
    def __init__(self):
        self.db = Database()
    
    def readAll(self):
        data = self.db.query("SELECT * FROM videojuego")
        return data