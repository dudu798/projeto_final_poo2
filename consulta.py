class Consulta:
    def __init__(self, id, paciente, medico, horario):
        self.id = id
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
    
    def descricao(self):
        return {
            'id': self.id,
            'paciente': self.paciente,
            'medico': self.medico,
            'horario': self.horario
            
        }
