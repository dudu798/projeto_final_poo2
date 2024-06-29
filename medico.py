from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, senha, CRM, Especialização):
        super().__init__(nome, senha)
        self.crm = CRM
        self.especializacao = Especialização

    def get_crm(self):
        return self.crm
    
    def set_crm(self, crm):
        self.crm = crm

    def get_nome(self):
        return self.nome

    def get_especializacao(self):
        return self.especializacao
    
    def set_especializacao(self, especializacao):
        self.especializacao = especializacao
        
    def descricao(self):
        return {'nome': self.nome, 'senha': self.senha_codificada, "CRM": self.crm, "Especialização": self.especializacao}
