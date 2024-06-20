from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, idade, crm, especializacao):
        super().__init__(nome, idade)
        self.crm = crm
        self.especializacao = especializacao

    def get_crm(self):
        return self.crm
    
    def set_crm(self, crm):
        self.crm = crm

    def get_especializacao(self):
        return self.especializacao
    
    def set_especializacao(self, especializacao):
        self.especializacao = especializacao
        
    def descricao(self):
        return f"{super().descricao()}, CRM: {self.crm}, Especialização: {self.especializacao}"