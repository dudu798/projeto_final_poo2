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
        pac1 = Paciente('Tadeu Toddy', 33, '97179468096' , 'S')
        self.lista_pacientes.append(pac1)

        pac2 = Paciente('Maria Silva', 45, '96858658092', 'N')
        self.lista_pacientes.append(pac2)

        pac3 = Paciente('João Oliveira', 28, '00566716011', 'S')
        self.lista_pacientes.append(pac3)

        pac4 = Paciente('Ana Souza', 50, '39940129025', 'N')
        self.lista_pacientes.append(pac4)

        pac5 = Paciente('Carlos Rocha', 62, '10491895070', 'S')
        self.lista_pacientes.append(pac5)

        med1 = Medico('Afonso Dino', 55, 204918951, 'Ortopedia')
        self.adicionar_medico('Afonso Dino', 'Ortopedia')
        self.lista_medicos.append(med1)

        med2 = Medico('Beatriz Lima', 40, 987654321, 'Pediatria')
        self.adicionar_medico('Beatriz Lima', 'Pediatria')
        self.lista_medicos.append(med2)

        med3 = Medico('Ricardo Santos', 48, 123456789, 'Cardiologia')
        self.adicionar_medico('Ricardo Santos', 'Cardiologia')
        self.lista_medicos.append(med3)

        med4 = Medico('Isabel Oliveira', 35, 876543210, 'Dermatologia')
        self.adicionar_medico('Isabel Oliveira', 'Dermatologia')
        self.lista_medicos.append(med4)

        med5 = Medico('Luciano Silva', 42, 543216789, 'Clinica')
        self.adicionar_medico('Luciano Silva', 'Clinica')
        self.lista_medicos.append(med5)

        med6 = Medico('Tatiane Costa', 50, 321654987, 'Endocrinologia')
        self.adicionar_medico('Tatiane Costa', 'Endocrinologia')
        self.lista_medicos.append(med6)

        med7 = Medico('Felipe Martins', 38, 987123456, 'Ortopedia')
        self.adicionar_medico('Felipe Martins', 'Ortopedia')
        self.lista_medicos.append(med7)

        med8 = Medico('Larissa Oliveira', 32, 654789321, 'Pediatria')
        self.adicionar_medico('Larissa Oliveira', 'Pediatria')
        self.lista_medicos.append(med8)

        med9 = Medico('Pedro Santos', 45, 789456123, 'Cardiologia')
        self.adicionar_medico('Pedro Santos', 'Cardiologia')
        self.lista_medicos.append(med9)

        med10 = Medico('Mariana Costa', 55, 321789654, 'Dermatologia')
        self.adicionar_medico('Mariana Costa', 'Dermatologia')
        self.lista_medicos.append(med10)

        med11 = Medico('Rafaela Lima', 42, 159753468, 'Endocrinologia')
        self.adicionar_medico('Rafaela Lima', 'Endocrinologia')
        self.lista_medicos.append(med11)
    

    def verifica_operacao(self,x,a,b,c,d,e,f,g,h,i):
        while x not in [a,b,c,d,e,f,g,h,i]:
            x = int(input('Operação inválida, digite novamente: '))
        return x

    def verifica_convenio(self, x):
        while x not in ['S','N']:
            x = input('Digite S se tiver plano ou N se não tiver: ').upper()
        return x

    def verifica_cpf(self, cpf):
        while True:
            cpf = ''.join(filter(str.isdigit, cpf))

            if len(cpf) != 11:
                print("CPF inválido. Por favor, digite novamente.")
                cpf = input("Digite o CPF: ")
                cpf = self.verifica_unicidade_cpf(cpf)
                continue
            
            soma = 0
            for i in range(9):
                soma += int(cpf[i]) * (10 - i)
            resto = soma % 11
            digito_verificador1 = 0 if resto < 2 else 11 - resto

            if digito_verificador1 != int(cpf[9]):
                print("CPF inválido. Por favor, digite novamente.")
                cpf = input("Digite o CPF: ")
                cpf = self.verifica_unicidade_cpf(cpf)
                continue

            soma = 0
            for i in range(10):
                soma += int(cpf[i]) * (11 - i)
            resto = soma % 11
            digito_verificador2 = 0 if resto < 2 else 11 - resto

            if digito_verificador2 != int(cpf[10]):
                print("CPF inválido. Por favor, digite novamente.")
                cpf = input("Digite o CPF: ")
                cpf = self.verifica_unicidade_cpf(cpf)
                continue
            break
        return cpf

    def verifica_unicidade_cpf(self, x):
        while x in self.lista_cpf:
            print('CPF já em uso. Por favor, digite novamente.')
            x = input('Digite o CPF: ')
            x = self.verifica_cpf(x)
        return x

    def verifica_crm(self, x):
        while (len(x) != 9) or (x in self.lista_crm):
            print('CRM inválida ou já em uso. Por favor, digite novamente.')
            x = input('Digite a CRM: ')
        return x
    
    def cadastrar_paciente(self, nome, idade, cpf, convenio):
        paciente = Paciente(nome,idade,cpf,convenio)
        self.lista_pacientes.append(paciente)
        self.lista_cpf.append(cpf)
        return paciente
    
    def cadastrar_medico(self, nome, idade, crm, especializacao):
        self.lista_crm.append(crm)
        especializacao = self.adicionar_medico(nome,especializacao)
        medico = Medico(nome,idade,crm,especializacao)
        self.lista_medicos.append(medico)
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
    
    def atualiza_paciente(self):
        cpf = input("Digite o CPF do paciente: ")
        paciente = next((p for p in self.lista_pacientes if p.cpf == cpf), None)
        if paciente:
            print('''
    1- Nome do paciente
    2- Idade do paciente
    3- CPF do paciente
    4- Sintoma do paciente
    5- Convenio do paciente
    ''')
            dado = int(input('Qual dado deseja alterar?: '))
            dado = self.verifica_operacao(dado, 1, 2, 3, 4, 5, 1, 1, 1, 1)
            if dado == 1:
                paciente.set_nome(input("Digite o novo nome do paciente: ").title())
            if dado == 2:
                paciente.set_idade(int(input("Digite a nova idade do paciente: ")))
            if dado == 3:
                alt_cpf = input("Digite o novo CPF do paciente: ")
                alt_cpf = self.verifica_cpf(alt_cpf)
                alt_cpf = self.verifica_unicidade_cpf(alt_cpf)
                paciente.set_cpf(alt_cpf)
            if dado == 4:
                paciente.set_sintomas(input("Digite todos os novos e antigos sintomas do paciente: "))
            if dado == 5:
                alt_con = paciente.set_convenio(input("Paciente possui plano de saúde? [S/N]: ").upper())
                alt_con = self.verifica_convenio(alt_con)
                paciente.set_convenio(alt_con)
            print('Dados do paciente foram alterados com sucesso!') 
            print(paciente.descricao())
            print(' ')
        else:
            print("Paciente não encontrado!")
            print(' ')
    
    def atualiza_medico(self):
        crm = input("Digite o CRM do médico: ") 
        medico = next((m for m in self.lista_medicos if m.crm == crm), None)
        if medico:
            print('''
    1- Nome do médico
    2- Idade do médico
    ''')
            dado = int(input('Qual dado deseja alterar?: '))
            dado = self.verifica_operacao(dado, 1, 2, 1, 1, 1, 1, 1, 1, 1)
            if dado == 1:
                medico.set_nome(input("Digite o novo nome do médico: ").title())
            if dado == 2:
                medico.set_idade(int(input("Digite a nova idade do médico: ")))

            print('Dados do médico foram alterados com sucesso!') 
            print(medico.descricao())
            print(f'Valor da consulta R$: 300.00')
            print(' ')
        else:
            print("Médico não encontrado!")
        
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
                "9- Mostrar faturamento do dia (fim da execução)"]
    
