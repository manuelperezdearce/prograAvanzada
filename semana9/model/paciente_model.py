from model.database import Database

class PacienteModel:
    
    def __init__(self):
        self.db = Database()
    
    def readAll(self):
        data = self.db.query("SELECT * FROM Pacientes")
        return data
    def insert(self, nombre, edad, genero, historial_medico, contacto):
        try:
            sql = "INSERT INTO Pacientes (nombre, edad, genero, historial_medico, contacto) VALUES (%s, %s, %s, %s, %s)"
            return self.db.execute(sql, (nombre, edad, genero, historial_medico, contacto))
        except Exception as e:
            print("Error al insertar paciente:", e)
            return None
    
    def delete(self, id_Paciente):
        self.db.execute("DELETE FROM Pacientes WHERE id = %s", (id_Paciente,))

    def find_by_id(self, id_Paciente):
        sql = "SELECT * FROM Pacientes WHERE id = %s"
        resultados = self.db.query(sql, (id_Paciente,))
        return resultados[0] if resultados else None
    
    def update(self, id_Paciente, nombre, edad, genero, historial_medico, contacto):
        sql = """
            UPDATE Pacientes 
            SET nombre = %s , edad=%s, genero = %s, historial_medico = %s, contacto = %s
            WHERE id = %s
        """
        self.db.execute(sql, (nombre, edad, genero, historial_medico, contacto, id_Paciente))
