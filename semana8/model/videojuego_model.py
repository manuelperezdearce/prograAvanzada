from model.database import Database

class VideojuegoModel:
    
    def __init__(self):
        self.db = Database()
    
    def readAll(self):
        data = self.db.query("SELECT * FROM videojuego")
        return data
    def insert(self, titulo, genero, clasificacion, plataforma):
        sql = "INSERT INTO videojuego (titulo, genero, clasificacion, plataforma) VALUES (%s, %s, %s, %s)"
        return self.db.execute(sql, (titulo, genero, clasificacion, plataforma))
    
    def delete(self, id_videojuego):
        self.db.execute("DELETE FROM videojuego WHERE id = %s", (id_videojuego,))

    def find_by_id(self, id_videojuego):
        sql = "SELECT * FROM videojuego WHERE id = %s"
        resultados = self.db.query(sql, (id_videojuego,))
        return resultados[0] if resultados else None
    
    def update(self, id_videojuego, titulo, genero, clasificacion, plataforma):
        sql = """
            UPDATE videojuego 
            SET titulo = %s, genero = %s, clasificacion = %s, plataforma = %s 
            WHERE id = %s
        """
        self.db.execute(sql, (titulo, genero, clasificacion, plataforma, id_videojuego))


