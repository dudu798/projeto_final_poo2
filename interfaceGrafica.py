import tkinter as tk
from tkinter import ttk, messagebox
from medico import Medico
from paciente import Paciente
from menu import Menu


class App():
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.janela_principal.title("Sistema de Gestão Hospitalar")
        self.menu = Menu()

    def criar_tela_menu(self):
        self.tela_menu = ttk.Frame(self.janela_principal, padding="10")
        self.tela_menu.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        opcoes = self.menu.mostrar_opcoes()
        for i, opcao in enumerate(opcoes):
            ttk.Label(self.tela_menu, text= opcao ).grid(column=0, row=i, sticky=tk.W)
            ttk.Button(self.tela_menu, text="Selecionar", command=lambda o=opcao: self.processar_opcao(o) ).grid(column=1, row=i, sticky=tk.E)

    def criar_tela_cadastro_paciente(self):
        self.tela_cadastro_paciente = ttk.Frame(self.janela_principal, padding="10")
        self.tela_cadastro_paciente.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(self.tela_cadastro_paciente, text="Nome").grid(column=0, row=1, sticky=tk.W)
        self.nome = ttk.Entry(self.tela_cadastro_paciente)
        self.nome.grid(column=1, row=1)

        ttk.Label(self.tela_cadastro_paciente, text="CPF").grid(column=0, row=2, sticky=tk.W)
        self.cpf = ttk.Entry(self.tela_cadastro_paciente)
        self.cpf.grid(column=1, row=2)

        ttk.Label(self.tela_cadastro_paciente, text="Idade").grid(column=0, row=3, sticky=tk.W)
        self.idade = ttk.Entry(self.tela_cadastro_paciente)
        self.idade.grid(column=1, row=3)

        self.valor_convenio = tk.StringVar()
        ttk.Label(self.tela_cadastro_paciente, text="Convênio").grid(column=0, row=4, sticky=tk.W)
        self.convenio = ttk.Radiobutton(self.tela_cadastro_paciente, text="Sim", variable=self.valor_convenio, value="Sim")
        self.convenio.grid(column=1, row=4)
        self.convenio = ttk.Radiobutton(self.tela_cadastro_paciente, text="Não",variable=self.valor_convenio, value="Não")
        self.convenio.grid(column=2, row=4)

        ttk.Button(self.tela_cadastro_paciente, text="Cadastrar", command= self.coletar_informacoes_paciente).grid(column=1, row=5)

    def coletar_informacoes_paciente(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        idade = self.idade.get()
        convenio = self.valor_convenio.get()

        paciente = self.menu.cadastrar_paciente(nome, cpf, idade, convenio)
        self.tela_cadastro_paciente.destroy()
        messagebox.showinfo("Paciente cadastrado!", f"Nome: {paciente.nome} \nCPF: {paciente.cpf} \nIdade: {paciente.idade} \nConvênio: {convenio}")

    def criar_tela_cadastro_medico(self):
        self.tela_cadastro_medico = ttk.Frame(self.janela_principal, padding="10")
        self.tela_cadastro_medico.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(self.tela_cadastro_medico, text="Nome").grid(column=0, row=1, sticky=tk.W)
        self.nome = ttk.Entry(self.tela_cadastro_medico)
        self.nome.grid(column=1, row=1)

        ttk.Label(self.tela_cadastro_medico, text="Idade").grid(column=0, row=2, sticky=tk.W)
        self.idade = ttk.Entry(self.tela_cadastro_medico)
        self.idade.grid(column=1, row=2)

        ttk.Label(self.tela_cadastro_medico, text="CRM").grid(column=0, row=3, sticky=tk.W)
        self.crm = ttk.Entry(self.tela_cadastro_medico)
        self.crm.grid(column=1, row=3)

        self.valor_especializacao = tk.StringVar()
        ttk.Label(self.tela_cadastro_medico, text="Especialização").grid(column=0, row=4, sticky=tk.W)
        self.especializacao = ttk.Radiobutton(self.tela_cadastro_medico, text="Ortopedia", variable=self.valor_especializacao, value="Ortopedia")
        self.especializacao.grid(column=1, row=4)
        self.especializacao = ttk.Radiobutton(self.tela_cadastro_medico, text="Pediatria",variable=self.valor_especializacao, value="Pediatria")
        self.especializacao.grid(column=2, row=4)
        self.especializacao = ttk.Radiobutton(self.tela_cadastro_medico, text="Cardiologia", variable=self.valor_especializacao, value="Cardiologia")
        self.especializacao.grid(column=3, row=4)
        self.especializacao = ttk.Radiobutton(self.tela_cadastro_medico, text="Dermatologia",variable=self.valor_especializacao, value="Dermatologia")
        self.especializacao.grid(column=4, row=4)
        self.especializacao = ttk.Radiobutton(self.tela_cadastro_medico, text="Endocrinologia",variable=self.valor_especializacao, value="Endocrinologia")
        self.especializacao.grid(column=5, row=4)

        ttk.Button(self.tela_cadastro_medico, text="Cadastrar", command= self.coletar_informacoes_medico).grid(column=1, row=5)

    def coletar_informacoes_medico(self):
        nome = self.nome.get()
        idade = self.idade.get()
        crm = self.crm.get()
        especializacao = self.valor_especializacao.get()

        medico = self.menu.cadastrar_medico(nome, idade, crm, especializacao)
        self.tela_cadastro_medico.destroy()
        messagebox.showinfo("Médico cadastrado!", f"Nome: {medico.nome} \nIdade: {medico.idade} \nCRM: {medico.crm}  \nEspecialização: {medico.especializacao}")

    def processar_opcao(self, opcao):
        
        if opcao == "1- Cadastrar um paciente":
            self.criar_tela_cadastro_paciente()

        if opcao == "2- Cadastrar um médico":
            self.criar_tela_cadastro_medico()

        if opcao == "3- Atualizar informações de algum paciente já cadastrado":
            self.atualiza_paciente()
            
        if opcao == "4- Atualizar informações de algum médico já cadastrado":
            self.atualiza_medico()

        if opcao == "5- Agendar uma consulta":
            self.agendar_consulta()

        if opcao == "6- Verificar consultas agendadas":
            nome_verifica_consulta = input("Digite o nome paciente para verificar as consultas: ").title()
            self.verificar_consulta(nome_verifica_consulta)
            
        if opcao == "7- Remarcar consultas":
            self.editar_consulta()
            
        if opcao == "8- Cancelar consultas":
            self.remover_consulta()
            
        if opcao == "9- Mostrar faturamento do dia (fim da execução)":
            faturamento_total = self.calcular_faturamento()
            print(f"Faturamento Total diário do Hospital: R${faturamento_total}")
