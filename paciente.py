from pessoa import Pessoa 

class Paciente(Pessoa):
    def __init__(self, nome, senha, cpf):
        super().__init__(nome,senha)
        self.cpf = cpf
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf
        
    def descricao(self):
        return f"{super().descricao()}, CPF: {self.cpf}, "
