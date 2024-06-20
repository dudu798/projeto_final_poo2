class Pessoa:
    def __init__(self ,nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade
        
    def descricao(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"