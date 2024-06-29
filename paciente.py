from pessoa import Pessoa 

class Paciente(Pessoa):
    def __init__(self, nome, senha, cpf):
        super().__init__(nome,senha)
        self.cpf = cpf
    
    def get_cpf(self):
        return self.cpf

    def get_nome(self):
        return self.nome
    
    def set_cpf(self, cpf):
        self.cpf = cpf
        
    def descricao(self):
        return {'nome': self.nome, 'senha': self.senha_codificada, 'cpf': self.cpf}
