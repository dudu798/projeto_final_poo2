#Classe Mãe
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

#Subclasses
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
    
#Funções Verifica
def verifica_operacao(x,a,b,c,d,e,f,g,h,i):
    while x not in [a,b,c,d,e,f,g,h,i]:
        x = int(input('Operação inválida, digite novamente: '))
    return x

def verifica_convenio(x):
  while x not in ['S','N']:
    x = input('Digite S se tiver plano ou N se não tiver: ').upper()
  return x

def verifica_cpf(cpf):
  while True:
      cpf = ''.join(filter(str.isdigit, cpf))

      if len(cpf) != 11:
          print("CPF inválido. Por favor, digite novamente.")
          cpf = input("Digite o CPF: ")
          cpf = unicidade_cpf(cpf)
          continue
     
      soma = 0
      for i in range(9):
          soma += int(cpf[i]) * (10 - i)
      resto = soma % 11
      digito_verificador1 = 0 if resto < 2 else 11 - resto

      if digito_verificador1 != int(cpf[9]):
          print("CPF inválido. Por favor, digite novamente.")
          cpf = input("Digite o CPF: ")
          cpf = unicidade_cpf(cpf)
          continue

      soma = 0
      for i in range(10):
          soma += int(cpf[i]) * (11 - i)
      resto = soma % 11
      digito_verificador2 = 0 if resto < 2 else 11 - resto

      if digito_verificador2 != int(cpf[10]):
          print("CPF inválido. Por favor, digite novamente.")
          cpf = input("Digite o CPF: ")
          cpf = unicidade_cpf(cpf)
          continue
      break
  return cpf

def unicidade_cpf(x):
    while x in lista_cpf:
        print('CPF já em uso. Por favor, digite novamente.')
        x=input('Digite o CPF: ')
        x=verifica_cpf(x)
    return x

def verificar_consulta(nome):
    consultas_paciente = [consulta for consulta in lista_consultas if consulta['nome_paciente'] == nome]

    if consultas_paciente:
        print()
        print(f"Consultas agendadas para o paciente {nome}:")
        for consulta in consultas_paciente:
            print()
            print(f"Médico: {consulta['nome_medico']}")
            print(f"Horário: {consulta['horario']}")
    else:
        print(f"Nenhuma consulta agendada para o paciente {nome}.")

def verifica_crm(x):
    while (len(x) != 9) or (x in lista_crm):
        print('CRM inválida ou já em uso. Por favor, digite novamente.')
        x=input('Digite a CRM: ')
    return x
    

#Funções Consultas
def agendar_consulta(x):
    print("Especializações disponíveis para consulta:")
    for i, especializacao in enumerate(especializacoes_medicas.keys(), start=1):
        print(f"{i} - {especializacao}")
    
    escolha_especializacao = int(input("Escolha a especialização (1 a 6): ")) - 1
    
    
    if 0 <= escolha_especializacao < len(especializacoes_medicas):
        especializacao = list(especializacoes_medicas.keys())[escolha_especializacao]
        print(f"\n{especializacao}s disponíveis para consulta:")
        for i, medico in enumerate(especializacoes_medicas[especializacao], start=1):
            print(f"  - Médico: {medico['nome']}")
            print(f"      Horários disponíveis: {', '.join(medico['horarios'])}")

        nome_medico = input("Digite o nome do médico desejado: ").title()
        horario_desejado = input("Digite o horário desejado (no formato HH:00): ")

        for medico in especializacoes_medicas[especializacao]:
            if medico['nome'] == nome_medico and horario_desejado in medico['horarios']:
                medico['horarios'].remove(horario_desejado)
                dic_consulta = {'nome_medico': nome_medico, 'horario': horario_desejado, 'nome_paciente': x}
                lista_consultas.append(dic_consulta)
                print(f"Consulta agendada com {nome_medico} às {horario_desejado}.")
                break
        else:
            print("Médico ou horário não encontrado. Consulta não agendada.")
    else:
        print("Escolha de especialização inválida.")

def remover_consulta():
    nome_paciente = input("Digite o nome do paciente para remover as consultas: ").title()

    consultas_remover = [consulta for consulta in lista_consultas if consulta['nome_paciente'] == nome_paciente]

    if consultas_remover:
        print(f"Consultas agendadas para o paciente {nome_paciente}:")
        for i, consulta in enumerate(consultas_remover, start=1):
            print(f"{i} - Médico: {consulta['nome_medico']}, Horário: {consulta['horario']}")

        escolha_consulta = int(input("Escolha o número da consulta que deseja remover: "))
        if 1 <= escolha_consulta <= len(consultas_remover):
            consulta_remover = lista_consultas.pop(lista_consultas.index(consultas_remover[escolha_consulta - 1]))
                                                   
            for medico in especializacoes_medicas.values():
                for m in medico:
                    if m['nome'] == consulta_remover['nome_medico']:
                        m['horarios'].append(consulta_remover['horario'])
                        break

            print("Consulta removida com sucesso!")
        else:
            print("Escolha de consulta inválida.")
    else:
        print(f"Nenhuma consulta agendada para o paciente {nome_paciente}.")
        
def editar_consulta():
    if lista_consultas:
        print("Consultas agendadas:")
        for i, consulta in enumerate(lista_consultas, start=1):
            print(f"{i} - Paciente: {consulta['nome_paciente']}, Médico: {consulta['nome_medico']}, Horário: {consulta['horario']}")
        
        escolha_consulta = int(input("Escolha o número da consulta que deseja editar: "))
        if 1 <= escolha_consulta <= len(lista_consultas):
            consulta_editar = lista_consultas[escolha_consulta - 1]
            novo_horario = input("Digite o novo horário (no formato HH:00): ")

            for medico in especializacoes_medicas.values():
                for m in medico:
                    if m['nome'] == consulta_editar['nome_medico']:
                        m['horarios'].append(consulta_editar['horario'])
                        break

            consulta_editar['horario'] = novo_horario

            for medico in especializacoes_medicas.values():
                for m in medico:
                    if m['nome'] == consulta_editar['nome_medico']:
                        m['horarios'].remove(novo_horario)
                        break

            print("Consulta editada com sucesso!")
        else:
            print("Escolha de consulta inválida.")
    else:
        print("Nenhuma consulta agendada.")

#Função adicionar especialização medica 
def adicionar_medico(x,y):
    if y in especializacoes_medicas:
        numeros_inteiros = list(range(8, 13)) + list(range(14, 19))
        horarios = [str(h) + ':00' for h in numeros_inteiros]
        especializacoes_medicas[y].append({'nome': x, 'horarios': horarios})
    while y not in especializacoes_medicas:
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
        
#Função para calculo do faturamento
def calcular_faturamento():
    valor_consulta = 300
    faturamento_total = 0

    for especializacao, medicos in especializacoes_medicas.items():
        for medico in medicos:
            faturamento_total += abs(len(medico['horarios'])-10)  * valor_consulta

    return faturamento_total

#Main

lista_pacientes = []
lista_medicos = []  
lista_consultas = []
lista_crm = []
lista_cpf = []
especializacoes_medicas = {'Ortopedia': [],'Pediatria': [],'Cardiologia': [],'Clinica': [],'Dermatologia': [],'Endocrinologia': []
}

#Exemplos de entrada
obj1 = Paciente('Tadeu Toddy', 33, '97179468096' , 'lesao muscular na panturrilha' , 'S')
lista_pacientes.append(obj1)

obj2 = Paciente('Maria Silva', 45, '96858658092', 'febre e dor de cabeça', 'N')
lista_pacientes.append(obj2)

obj3 = Paciente('João Oliveira', 28, '00566716011', 'tosse persistente', 'S')
lista_pacientes.append(obj3)

obj4 = Paciente('Ana Souza', 50, '39940129025', 'dores abdominais', 'N')
lista_pacientes.append(obj4)

obj5 = Paciente('Carlos Rocha', 62, '10491895070', 'fadiga e falta de ar', 'S')
lista_pacientes.append(obj5)

med1 = Medico('Afonso Dino', 55, 204918951, 'Ortopedia')
adicionar_medico('Afonso Dino', 'Ortopedia')
lista_medicos.append(med1)

med2 = Medico('Beatriz Lima', 40, 987654321, 'Pediatria')
adicionar_medico('Beatriz Lima', 'Pediatria')
lista_medicos.append(med2)

med3 = Medico('Ricardo Santos', 48, 123456789, 'Cardiologia')
adicionar_medico('Ricardo Santos', 'Cardiologia')
lista_medicos.append(med3)

med4 = Medico('Isabel Oliveira', 35, 876543210, 'Dermatologia')
adicionar_medico('Isabel Oliveira', 'Dermatologia')
lista_medicos.append(med4)

med5 = Medico('Luciano Silva', 42, 543216789, 'Clinica')
adicionar_medico('Luciano Silva', 'Clinica')
lista_medicos.append(med5)

med6 = Medico('Tatiane Costa', 50, 321654987, 'Endocrinologia')
adicionar_medico('Tatiane Costa', 'Endocrinologia')
lista_medicos.append(med6)
med7 = Medico('Felipe Martins', 38, 987123456, 'Ortopedia')
adicionar_medico('Felipe Martins', 'Ortopedia')
lista_medicos.append(med7)

med8 = Medico('Larissa Oliveira', 32, 654789321, 'Pediatria')
adicionar_medico('Larissa Oliveira', 'Pediatria')
lista_medicos.append(med8)

med9 = Medico('Pedro Santos', 45, 789456123, 'Cardiologia')
adicionar_medico('Pedro Santos', 'Cardiologia')
lista_medicos.append(med9)

med10 = Medico('Mariana Costa', 55, 321789654, 'Dermatologia')
adicionar_medico('Mariana Costa', 'Dermatologia')
lista_medicos.append(med10)

med11 = Medico('Rafaela Lima', 42, 159753468, 'Endocrinologia')
adicionar_medico('Rafaela Lima', 'Endocrinologia')
lista_medicos.append(med11)

while True:
    
    print('''------------------------------------------------------------------------------------
1- Cadastrar um paciente
2- Cadastrar um médico
3- Atualizar informações de algum paciente já cadastrado
4- Atualizar informações de algum médico já cadastrado
5- Agendar uma consulta
6- Verificar consultas agendadas
7- Remarcar consultas
8- Cancelar consultas
9- Mostrar faturamento do dia (fim da execução)
------------------------------------------------------------------------------------''')
  
    operacao = int(input("Qual operação deseja fazer?: "))
    operacao = verifica_operacao(operacao, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
  
    if operacao == 1:
        nome = input('Nome do paciente: ').title()
        cpf = input('CPF do paciente: ')
        cpf = verifica_cpf(cpf)
        cpf = unicidade_cpf(cpf)
        lista_cpf.append(cpf)
        
        idade = int(input('Idade do paciente: '))
        sintomas = input('Sintomas que o paciente apresenta: ')
        convenio = input('Paciente possui plano de saúde? [S/N]: ').upper()
        convenio = verifica_convenio(convenio)
        paciente=Paciente(nome,idade,cpf,sintomas,convenio)
        lista_pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")
        print(paciente.descricao())
        print(' ')

    if operacao == 2:
        nome = input('Nome do médico: ').title()
        idade = int(input('Idade do médico: '))
        crm = input('CRM do médico (9 dígitos numéricos): ')
        crm = verifica_crm(crm)
        lista_crm.append(crm)
        print('''
Especializações disponíveis:
        -Ortopedia
        -Pediatria
        -Cardiologia
        -Clinica
        -Dermatologia
        -Endocrinologia
        ''')
        especializacao = input('Qual especialização: ').title()
        especializacao = adicionar_medico(nome,especializacao)
        medico=Medico(nome,idade,crm,especializacao)
        lista_medicos.append(medico)
        print("Médico cadastrado com sucesso!")
        print(medico.descricao())
        print(f'Valor da consulta R$: 300.00')
        print(' ')

    if operacao == 3:
        cpf = input("Digite o CPF do paciente: ")
        paciente = next((p for p in lista_pacientes if p.cpf == cpf), None)
        if paciente:
            print('''
1- Nome do paciente
2- Idade do paciente
3- CPF do paciente
4- Sintoma do paciente
5- Convenio do paciente
''')
            dado=int(input('Qual dado deseja alterar?: '))
            dado=verifica_operacao(dado, 1, 2, 3, 4, 5, 1, 1, 1, 1)
            if dado == 1:
                paciente.set_nome(input("Digite o novo nome do paciente: ").title())
            if dado == 2:
                paciente.set_idade(int(input("Digite a nova idade do paciente: ")))
            if dado == 3:
                alt_cpf = input("Digite o novo CPF do paciente: ")
                alt_cpf = verifica_cpf(alt_cpf)
                alt_cpf = unicidade_cpf(alt_cpf)
                paciente.set_cpf(alt_cpf)
            if dado == 4:
                paciente.set_sintomas(input("Digite todos os novos e antigos sintomas do paciente: "))
            if dado == 5:
                alt_con = paciente.set_convenio(input("Paciente possui plano de saúde? [S/N]: ").upper())
                alt_con = verifica_convenio(alt_con)
                paciente.set_convenio(alt_con)
            print('Dados do paciente foram alterados com sucesso!') 
            print(paciente.descricao())
            print(' ')
        else:
            print("Paciente não encontrado!")
            print(' ')
        
    if operacao == 4:
        crm = input("Digite o CRM do médico: ") 
        medico = next((m for m in lista_medicos if m.crm == crm), None)
        if medico:
            print('''
1- Nome do médico
2- Idade do médico
''')
            dado=int(input('Qual dado deseja alterar?: '))
            dado=verifica_operacao(dado, 1, 2, 1, 1, 1, 1, 1, 1, 1)
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

    if operacao == 5:
        cpf_paciente = input("Digite o CPF do paciente que deseja marcar uma consulta: ")
        existe = False
        for pacien in lista_pacientes:
            if cpf_paciente == pacien.get_cpf():
                agendar_consulta(pacien.get_nome())
                existe = True
        if not existe:
            print("CPF não cadastrado!")

    if operacao == 6:
        nome_verifica_consulta = input("Digite o nome paciente para verificar as consultas: ").title()
        verificar_consulta(nome_verifica_consulta)
        
    if operacao == 7:
        editar_consulta()
        
    if operacao == 8:
        remover_consulta()
        
    if operacao == 9:
        faturamento_total = calcular_faturamento()
        print(f"Faturamento Total diário do Hospital: R${faturamento_total}")
        break
