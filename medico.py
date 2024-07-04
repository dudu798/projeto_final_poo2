from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, senha, CRM, Especialização, horarios=None):
        super().__init__(nome, senha)
        self.crm = CRM
        self.especializacao = Especialização
        if horarios is None:
            self.horarios = [str(h) + ':00' for h in list(range(8, 13)) + list(range(14, 19))]
        else:
            self.horarios = horarios
        

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
        
    def get_horarios(self):
        return self.horarios

    def adicionar_horario(self, horario):
        self.horarios.append(horario)

    def remover_horario(self, horario):
        if horario in self.horarios:
            self.horarios.remove(horario)

    def descricao(self):
        return {
            'nome': self.nome,
            'senha': self.senha_codificada,
            'CRM': self.crm,
            'Especialização': self.especializacao,
            'horarios': self.horarios
        }
