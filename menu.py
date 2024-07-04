import json
from paciente import Paciente
from medico import Medico
from consulta import Consulta

class Menu:
    def __init__(self):
        self.lista_pacientes = []
        self.lista_medicos = []  
        self.lista_consultas = []
        self.lista_crm = []
        self.lista_cpf = []

        self.especializacoes_medicas = {'Ortopedia': [],'Pediatria': [],'Cardiologia': [],'Clinica': [],'Dermatologia': [],'Endocrinologia': []}
        
        self.carregar_dados()
    
    def carregar_dados(self):
        try:
            with open('dados_pacientes.json', 'r') as file:
                dados = json.load(file)
                self.lista_pacientes = [Paciente(**dados_paciente) for dados_paciente in dados['pacientes']]
                self.lista_cpf = dados.get('cpfs', [])
        except FileNotFoundError:
            self.lista_pacientes = []
            self.lista_cpf = []

        try:
            with open('dados_medicos.json', 'r') as file:
                dados = json.load(file)
                if 'medicos' in dados:  # Verifica se há dados de médicos no arquivo
                    self.lista_medicos = [Medico(**dados_medico) for dados_medico in dados['medicos']]
                    self.lista_crm = dados.get('crms', [])
    
        except FileNotFoundError:
            self.lista_medicos = []
            self.lista_crm = []
            
        try:
            with open('dados_consultas.json', 'r') as file:
                dados = json.load(file)
                self.lista_consultas = [Consulta(**dados_consulta) for dados_consulta in dados['consultas']]
            
        except FileNotFoundError:
            self.lista_consultas = []

    def salvar_dados(self):
        dados_paciente = [paciente.descricao() for paciente in self.lista_pacientes]
        dados_medico = [medico.descricao() for medico in self.lista_medicos]
        dados_consulta = [consulta.descricao() for consulta in self.lista_consultas]

        with open('dados_pacientes.json', 'w') as file:
            json.dump({'pacientes': dados_paciente, 'cpfs': self.lista_cpf}, file, indent=4)
        
        with open('dados_medicos.json', 'w') as file:
            json.dump({'medicos': dados_medico, 'crms': self.lista_crm}, file, indent=4)
            
        with open('dados_consultas.json', 'w') as file:
            json.dump({'consultas': dados_consulta}, file, indent=4)

    def mostrar_opcoes(self):
        return ["1- Cadastrar um paciente", "2- Cadastrar um médico",
                "3- Atualizar informações de algum paciente já cadastrado",
                "4- Atualizar informações de algum médico já cadastrado",
                "5- Agendar uma consulta", "6- Verificar consultas agendadas",
                "7- Remarcar consultas", "8- Cancelar consultas",
                "9- Ver contas cadastradas"]
    
    def verifica_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            return False
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        digito_verificador1 = 0 if resto < 2 else 11 - resto
        if digito_verificador1 != int(cpf[9]):
            return False
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        digito_verificador2 = 0 if resto < 2 else 11 - resto
        if digito_verificador2 != int(cpf[10]):
            return False
        return True
    
    def cadastrar_paciente(self, nome, senha, cpf):
        paciente = Paciente(nome, senha, cpf)
        self.lista_pacientes.append(paciente)
        self.lista_cpf.append(cpf)
        self.salvar_dados()
        return paciente
    
    def cadastrar_medico(self, nome, senha, crm, especializacao):
        self.lista_crm.append(crm)
        especializacao = self.adicionar_medico(nome,especializacao)
        medico = Medico(nome,senha,crm,especializacao)
        self.lista_medicos.append(medico)
        self.salvar_dados()
        return medico

    def adicionar_medico(self, x, y):
        if y in self.especializacoes_medicas:
            numeros_inteiros = list(range(8, 13)) + list(range(14, 19))
            horarios = [str(h) + ':00' for h in numeros_inteiros]
            self.especializacoes_medicas[y].append({'nome': x, 'horarios': horarios})
        while y not in self.especializacoes_medicas:
            print("O Hospital não trabalha com essa área.")
            print('''Especializações disponíveis:
            -Ortopedia
            -Pediatria
            -Cardiologia
            -Clinica
            -Dermatologia
            -Endocrinologia
            ''')
            y = input('Digite uma especialização que o hospital trabalhe: ').title()
        return y
        
    def agendar_consulta_interface(self, cpf_paciente, especializacao, nome_medico, horario_desejado):
        self.carregar_dados()
        for paciente in self.lista_pacientes:
            if cpf_paciente == paciente.get_cpf():
                nome_paciente = paciente.get_nome()
                for medico in self.lista_medicos:
                    if medico.get_nome() == nome_medico and medico.get_especializacao() == especializacao:
                        if horario_desejado in medico.get_horarios():
                            medico.remover_horario(horario_desejado)
                            consulta = Consulta(len(self.lista_consultas) + 1, nome_paciente, nome_medico, horario_desejado)
                            self.lista_consultas.append(consulta)
                            self.salvar_dados()
                            return True
        return False

    def verificar_consulta(self, nome_paciente):
        consultas_paciente = [consulta for consulta in self.lista_consultas if consulta.paciente == nome_paciente]
        if consultas_paciente:
            return [{"nome_medico": consulta.medico, "horario": consulta.horario} for consulta in consultas_paciente]
        return None

    def editar_consulta_interface(self, nome_paciente, nome_medico, novo_horario):
        for consulta in self.lista_consultas:
            if consulta.paciente == nome_paciente and consulta.medico == nome_medico:
                for medico in self.lista_medicos:
                    if medico.get_nome() == nome_medico:
                        medico.adicionar_horario(consulta.horario)
                        medico.remover_horario(novo_horario)
                        consulta.horario = novo_horario
                        self.salvar_dados()
                        return True
        return False

    def remover_consulta_interface(self, nome_paciente):
        for consulta in self.lista_consultas:
            if consulta.paciente == nome_paciente:
                for medico in self.lista_medicos:
                    if medico.get_nome() == consulta.medico:
                        medico.adicionar_horario(consulta.horario)
                        break
                self.lista_consultas.remove(consulta)
                self.salvar_dados()
                return True
        return False
    
