import hashlib

class Pessoa:
    def __init__(self ,nome, senha):
        self.nome = nome
        self.senha_codificada = self.codifica_senha(senha)

    def codifica_senha(self, senha):
        h = hashlib.sha256()   # Algoritmo de encodificação SHA256
        h.update(senha.encode())    # Torna senha fornecida em bytes
        return h.hexdigest() # Converte byter em uma string hexadecimal
