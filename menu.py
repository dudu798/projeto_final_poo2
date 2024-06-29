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
                self.lista_medicos = [Medico(**dados_medico) for dados_medico in dados['medicos']]
                self.lista_crm = dados.get('crms', [])
        except FileNotFoundError:
            self.lista_medicos = []
            self.lista_crm = []

    def salvar_dados(self):
        dados_paciente = [paciente.descricao() for paciente in self.lista_pacientes]
        dados_medico = [medico.descricao() for medico in self.lista_medicos]

        with open('dados_pacientes.json', 'w') as file:
            json.dump({'pacientes': dados_paciente, 'cpfs': self.lista_cpf}, file, indent=4)
        
        with open('dados_medicos.json', 'w') as file:
            json.dump({'medicos': dados_medico, 'crms': self.lista_crm}, file, indent=4)

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
        for paciente in self.lista_pacientes:
            if cpf_paciente == paciente.get_cpf():
                if especializacao in self.especializacoes_medicas:
                    for medico in self.especializacoes_medicas[especializacao]:
                        if medico['nome'] == nome_medico and horario_desejado in medico['horarios']:
                            medico['horarios'].remove(horario_desejado)
                            consulta = Consulta(len(self.lista_consultas) + 1, paciente, nome_medico, horario_desejado)
                            self.lista_consultas.append(consulta)
                            return True
        return False

    def verificar_consulta(self, nome_paciente):
        consultas_paciente = [consulta for consulta in self.lista_consultas if consulta.paciente.get_nome() == nome_paciente]
        if consultas_paciente:
            return [{"nome_medico": consulta.medico, "horario": consulta.horario} for consulta in consultas_paciente]
        return None

    def editar_consulta_interface(self, nome_paciente, nome_medico, novo_horario):
        for consulta in self.lista_consultas:
            if consulta.paciente.get_nome() == nome_paciente and consulta.medico == nome_medico:
                for medico in self.especializacoes_medicas.values():
                    for m in medico:
                        if m['nome'] == nome_medico:
                            m['horarios'].append(consulta.horario)
                            break
                consulta.horario = novo_horario
                for medico in self.especializacoes_medicas.values():
                    for m in medico:
                        if m['nome'] == nome_medico:
                            if novo_horario in m['horarios']:
                                m['horarios'].remove(novo_horario)
                                return True
        return False

    def remover_consulta_interface(self, nome_paciente):
        consultas_remover = [consulta for consulta in self.lista_consultas if consulta.paciente.get_nome() == nome_paciente]
        if consultas_remover:
            consulta_remover = consultas_remover[0]
            self.lista_consultas.remove(consulta_remover)
            for medico in self.especializacoes_medicas.values():
                for m in medico:
                    if m['nome'] == consulta_remover.medico:
                        m['horarios'].append(consulta_remover.horario)
                        return True
        return False
    
