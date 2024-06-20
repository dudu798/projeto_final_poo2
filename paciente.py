from pessoa import Pessoa 

class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf, sintomas, convenio):
        super().__init__(nome,idade)
        self.cpf = cpf
        self.sintomas = sintomas
        self.convenio = convenio
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_sintomas(self):
        return self.sintomas
    
    def set_sintomas(self, sintomas):
        self.sintomas = sintomas

    def get_convenio(self):
        return self.convenio
    
    def set_convenio(self, convenio):
        self.convenio = convenio
        
    def descricao(self):
        return f"{super().descricao()}, CPF: {self.cpf}, Sintomas: {self.sintomas}, Convênio: {self.convenio}"