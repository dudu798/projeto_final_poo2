from paciente import Paciente
from medico import Medico

class Menu:
    def __init__(self):
        self.lista_pacientes = []
        self.lista_medicos = []  
        self.lista_consultas = []
        self.lista_crm = []
        self.lista_cpf = []

        self.especializacoes_medicas = {'Ortopedia': [],'Pediatria': [],'Cardiologia': [],'Clinica': [],'Dermatologia': [],'Endocrinologia': []}
        pac1 = Paciente('Tadeu Toddy', "12345", '97179468096')
        self.lista_pacientes.append(pac1)

        pac2 = Paciente('Maria Silva', "12345", '96858658092')
        self.lista_pacientes.append(pac2)

        pac3 = Paciente('João Oliveira', "12345", '00566716011')
        self.lista_pacientes.append(pac3)

        pac4 = Paciente('Ana Souza', "12345", '39940129025')
        self.lista_pacientes.append(pac4)

        pac5 = Paciente('Carlos Rocha', "12345", '10491895070')
        self.lista_pacientes.append(pac5)

        med1 = Medico('Afonso Dino', "12345", 204918951, 'Ortopedia')
        self.adicionar_medico('Afonso Dino', 'Ortopedia')
        self.lista_medicos.append(med1)

        med2 = Medico('Beatriz Lima', "12345", 987654321, 'Pediatria')
        self.adicionar_medico('Beatriz Lima', 'Pediatria')
        self.lista_medicos.append(med2)

        med3 = Medico('Ricardo Santos', "12345", 123456789, 'Cardiologia')
        self.adicionar_medico('Ricardo Santos', 'Cardiologia')
        self.lista_medicos.append(med3)

        med4 = Medico('Isabel Oliveira', "12345", 876543210, 'Dermatologia')
        self.adicionar_medico('Isabel Oliveira', 'Dermatologia')
        self.lista_medicos.append(med4)

        med5 = Medico('Luciano Silva', "12345", 543216789, 'Clinica')
        self.adicionar_medico('Luciano Silva', 'Clinica')
        self.lista_medicos.append(med5)

        med6 = Medico('Tatiane Costa', "12345", 321654987, 'Endocrinologia')
        self.adicionar_medico('Tatiane Costa', 'Endocrinologia')
        self.lista_medicos.append(med6)

        med7 = Medico('Felipe Martins', "12345", 987123456, 'Ortopedia')
        self.adicionar_medico('Felipe Martins', 'Ortopedia')
        self.lista_medicos.append(med7)

        med8 = Medico('Larissa Oliveira', "12345", 654789321, 'Pediatria')
        self.adicionar_medico('Larissa Oliveira', 'Pediatria')
        self.lista_medicos.append(med8)

        med9 = Medico('Pedro Santos', "12345", 789456123, 'Cardiologia')
        self.adicionar_medico('Pedro Santos', 'Cardiologia')
        self.lista_medicos.append(med9)

        med10 = Medico('Mariana Costa', "12345", 321789654, 'Dermatologia')
        self.adicionar_medico('Mariana Costa', 'Dermatologia')
        self.lista_medicos.append(med10)

        med11 = Medico('Rafaela Lima', "12345", 159753468, 'Endocrinologia')
        self.adicionar_medico('Rafaela Lima', 'Endocrinologia')
        self.lista_medicos.append(med11)

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
        return paciente
    
    def cadastrar_medico(self, nome, senha, crm, especializacao):
        self.lista_crm.append(crm)
        especializacao = self.adicionar_medico(nome,especializacao)
        medico = Medico(nome,senha,crm,especializacao)
        self.lista_medicos.append(medico)
        return medico
    
    def atualizar_paciente(self, cpf_atualizar, valor_mudanca, novo_valor):
        for paciente in self.lista_pacientes:
            if paciente.cpf == cpf_atualizar:
                if valor_mudanca == "Nome":
                    paciente.nome = novo_valor
                elif valor_mudanca == "CPF":
                    paciente.cpf = novo_valor
                elif valor_mudanca == "Idade":
                    paciente.idade = novo_valor
                elif valor_mudanca == "Convenio":
                    paciente.convenio = novo_valor
                return paciente
        return None
    
    def atualizar_medico(self, crm_atualizar, valor_mudanca, novo_valor):
        for medico in self.lista_medicos:
            if medico.crm == crm_atualizar:
                if valor_mudanca == "Nome":
                    medico.nome = novo_valor
                elif valor_mudanca == "CRM":
                    medico.crm = novo_valor
                elif valor_mudanca == "Idade":
                    medico.idade = novo_valor
                return medico
        return None

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
        
    def agendar_consulta(self):
        cpf_paciente = input("Digite o CPF do paciente que deseja marcar uma consulta: ")
        existe = False
        for paciente in self.lista_pacientes:
            if cpf_paciente == paciente.get_cpf():
                print("Especializações disponíveis para consulta:")
                for i, especializacao in enumerate(self.especializacoes_medicas.keys(), start=1):
                    print(f"{i} - {especializacao}")
                
                escolha_especializacao = int(input("Escolha a especialização (1 a 6): ")) - 1
                
                
                if 0 <= escolha_especializacao < len(self.especializacoes_medicas):
                    especializacao = list(self.especializacoes_medicas.keys())[escolha_especializacao]
                    print(f"\n{especializacao}s disponíveis para consulta:")
                    for i, medico in enumerate(self.especializacoes_medicas[especializacao], start=1):
                        print(f"  - Médico: {medico['nome']}")
                        print(f"      Horários disponíveis: {', '.join(medico['horarios'])}")

                    nome_medico = input("Digite o nome do médico desejado: ").title()
                    horario_desejado = input("Digite o horário desejado (no formato HH:00): ")

                    for medico in self.especializacoes_medicas[especializacao]:
                        if medico['nome'] == nome_medico and horario_desejado in medico['horarios']:
                            medico['horarios'].remove(horario_desejado)
                            dic_consulta = {'nome_medico': nome_medico, 'horario': horario_desejado, 'nome_paciente': paciente.get_nome()}
                            self.lista_consultas.append(dic_consulta)
                            print(f"Consulta agendada com {nome_medico} às {horario_desejado}.")
                            break
                    else:
                        print("Médico ou horário não encontrado. Consulta não agendada.")
                else:
                    print("Escolha de especialização inválida.")

                existe = True
        if not existe:
            print("CPF não cadastrado!")
    
    def verificar_consulta(self, nome):
        consultas_paciente = [consulta for consulta in self.lista_consultas if consulta['nome_paciente'] == nome]

        if consultas_paciente:
            print()
            print(f"Consultas agendadas para o paciente {nome}:")
            for consulta in consultas_paciente:
                print()
                print(f"Médico: {consulta['nome_medico']}")
                print(f"Horário: {consulta['horario']}")
        else:
            print(f"Nenhuma consulta agendada para o paciente {nome}.")
    
    def editar_consulta(self):
        if self.lista_consultas:
            print("Consultas agendadas:")
            for i, consulta in enumerate(self.lista_consultas, start=1):
                print(f"{i} - Paciente: {consulta['nome_paciente']}, Médico: {consulta['nome_medico']}, Horário: {consulta['horario']}")
            
            escolha_consulta = int(input("Escolha o número da consulta que deseja editar: "))
            if 1 <= escolha_consulta <= len(self.lista_consultas):
                consulta_editar = self.lista_consultas[escolha_consulta - 1]
                novo_horario = input("Digite o novo horário (no formato HH:00): ")

                for medico in self.especializacoes_medicas.values():
                    for m in medico:
                        if m['nome'] == consulta_editar['nome_medico']:
                            m['horarios'].append(consulta_editar['horario'])
                            break

                consulta_editar['horario'] = novo_horario

                for medico in self.especializacoes_medicas.values():
                    for m in medico:
                        if m['nome'] == consulta_editar['nome_medico']:
                            m['horarios'].remove(novo_horario)
                            break

                print("Consulta editada com sucesso!")
            else:
                print("Escolha de consulta inválida.")
        else:
            print("Nenhuma consulta agendada.")
    
    def remover_consulta(self):
        nome_paciente = input("Digite o nome do paciente para remover as consultas: ").title()

        consultas_remover = [consulta for consulta in self.lista_consultas if consulta['nome_paciente'] == nome_paciente]

        if consultas_remover:
            print(f"Consultas agendadas para o paciente {nome_paciente}:")
            for i, consulta in enumerate(consultas_remover, start=1):
                print(f"{i} - Médico: {consulta['nome_medico']}, Horário: {consulta['horario']}")

            escolha_consulta = int(input("Escolha o número da consulta que deseja remover: "))
            if 1 <= escolha_consulta <= len(consultas_remover):
                consulta_remover = self.lista_consultas.pop(self.lista_consultas.index(consultas_remover[escolha_consulta - 1]))
                                                    
                for medico in self.especializacoes_medicas.values():
                    for m in medico:
                        if m['nome'] == consulta_remover['nome_medico']:
                            m['horarios'].append(consulta_remover['horario'])
                            break

                print("Consulta removida com sucesso!")
            else:
                print("Escolha de consulta inválida.")
        else:
            print(f"Nenhuma consulta agendada para o paciente {nome_paciente}.")
        
        

    def calcular_faturamento(self):
        valor_consulta = 300
        faturamento_total = 0

        for medicos in self.especializacoes_medicas.items():
            for medico in medicos:
                faturamento_total += abs(len(medico['horarios'])-10)  * valor_consulta

        return faturamento_total
    
    def mostrar_opcoes(self):
        return ["1- Cadastrar um paciente", "2- Cadastrar um médico",
                "3- Atualizar informações de algum paciente já cadastrado",
                "4- Atualizar informações de algum médico já cadastrado",
                "5- Agendar uma consulta", "6- Verificar consultas agendadas",
                "7- Remarcar consultas", "8- Cancelar consultas",
                "9- Mostrar faturamento do dia (fim da execução)", "10- Ver pacientes cadastrados"]
    
