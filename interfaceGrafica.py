import tkinter as tk
from tkinter import ttk, messagebox
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

        ttk.Label(self.tela_cadastro_paciente, text="Senha").grid(column=0, row=2, sticky=tk.W)
        self.senha = ttk.Entry(self.tela_cadastro_paciente)
        self.senha.grid(column=1, row=2)

        ttk.Label(self.tela_cadastro_paciente, text="CPF").grid(column=0, row=3, sticky=tk.W)
        self.cpf = ttk.Entry(self.tela_cadastro_paciente)
        self.cpf.grid(column=1, row=3)

        ttk.Button(self.tela_cadastro_paciente, text="Cadastrar", command= self.coletar_informacoes_paciente).grid(column=1, row=5)
        
    def coletar_informacoes_paciente(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        senha = self.senha.get()

        if self.menu.verifica_cpf(cpf) and cpf not in self.menu.lista_cpf and len(senha) >= 8:
            paciente = self.menu.cadastrar_paciente(nome, senha, cpf)
            self.tela_cadastro_paciente.destroy()
            messagebox.showinfo("Paciente cadastrado!", f"Nome: {paciente.nome} \nSenha: {paciente.senha_codificada}\nCPF: {paciente.cpf}")
       
        elif not self.menu.verifica_cpf(cpf) or cpf in self.menu.lista_cpf:
            messagebox.showerror("Erro", "CPF inválido")

        elif len(senha) < 8:
            messagebox.showerror("Erro","Senha inválida, mínimo de 8 dígitos" )
        

    def criar_tela_cadastro_medico(self):
        self.tela_cadastro_medico = ttk.Frame(self.janela_principal, padding="10")
        self.tela_cadastro_medico.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(self.tela_cadastro_medico, text="Nome").grid(column=0, row=1, sticky=tk.W)
        self.nome = ttk.Entry(self.tela_cadastro_medico)
        self.nome.grid(column=1, row=1)

        ttk.Label(self.tela_cadastro_medico, text="Senha").grid(column=0, row=2, sticky=tk.W)
        self.senha = ttk.Entry(self.tela_cadastro_medico)
        self.senha.grid(column=1, row=2)

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
        senha = self.senha.get()
        crm = self.crm.get()
        especializacao = self.valor_especializacao.get()

        if len(crm) == 9 and crm not in self.menu.lista_crm and len(senha) >= 8:
            medico = self.menu.cadastrar_medico(nome, senha, crm, especializacao)
            self.tela_cadastro_medico.destroy()
            messagebox.showinfo("Médico cadastrado!", f"Nome: {medico.nome} \nSenha: {medico.senha_codificada} \nCRM: {medico.crm}  \nEspecialização: {medico.especializacao}")
        
        elif len(crm) != 9 or crm in self.menu.lista_crm:
            messagebox.showerror("Erro", "CRM inválido")

        elif len(senha) < 8:
            messagebox.showerror("Erro","Senha inválida, mínimo de 8 dígitos" )


    def criar_tela_atualiza_paciente(self):
        self.tela_atualiza_paciente = ttk.Frame(self.janela_principal, padding="10")
        self.tela_atualiza_paciente.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.valor_mudanca = tk.StringVar()
        self.escolher_mudanca = ttk.Radiobutton(self.tela_atualiza_paciente, text="Nome", variable=self.valor_mudanca, value="Nome")
        self.escolher_mudanca.grid(column=1, row=1)
        self.escolher_mudanca = ttk.Radiobutton(self.tela_atualiza_paciente, text="Senha", variable=self.valor_mudanca, value="Senha")
        self.escolher_mudanca.grid(column=2, row=1)
        self.escolher_mudanca = ttk.Radiobutton(self.tela_atualiza_paciente, text="CPF", variable=self.valor_mudanca, value="CPF")
        self.escolher_mudanca.grid(column=3, row=1)

        ttk.Label(self.tela_atualiza_paciente, text="CPF do paciente a ser atualizado:").grid(column=0, row=0, sticky=tk.W)
        self.cpf_atualizar = ttk.Entry(self.tela_atualiza_paciente)
        self.cpf_atualizar.grid(column=1, row=0)

        ttk.Button(self.tela_atualiza_paciente, text="Próximo", command=self.coletar_informacoes_atualiza_paciente).grid(column=1, row=6)
    
    def coletar_informacoes_atualiza_paciente(self):
        cpf_atualizar = self.cpf_atualizar.get()
        valor_mudanca = self.valor_mudanca.get()

        if valor_mudanca == "Nome":
            ttk.Label(self.tela_atualiza_paciente, text="Novo nome").grid(column=0, row=7, sticky=tk.W)
            self.novo_nome = ttk.Entry(self.tela_atualiza_paciente)
            self.novo_nome.grid(column=1, row=7)
            ttk.Button(self.tela_atualiza_paciente, text="Atualizar", command=lambda: self.atualizar_paciente(cpf_atualizar,valor_mudanca,self.novo_nome.get())).grid(column=1, row=8)
        
        elif valor_mudanca == "CPF":
            ttk.Label(self.tela_atualiza_paciente, text="Novo CPF").grid(column=0, row=7, sticky=tk.W)
            self.novo_cpf = ttk.Entry(self.tela_atualiza_paciente)
            self.novo_cpf.grid(column=1, row=7)
            ttk.Button(self.tela_atualiza_paciente, text="Atualizar", command=lambda: self.atualizar_paciente(cpf_atualizar, valor_mudanca, self.novo_cpf.get())).grid(column=1, row=8)

        elif valor_mudanca == "Senha":
            ttk.Label(self.tela_atualiza_paciente, text="Nova senha:").grid(column=0, row=7, sticky=tk.W)
            self.nova_senha = ttk.Entry(self.tela_atualiza_paciente)
            self.nova_senha.grid(column=1, row=7)
            ttk.Button(self.tela_atualiza_paciente, text="Atualizar", command=lambda: self.atualizar_paciente(cpf_atualizar, valor_mudanca, self.nova_senha.get())).grid(column=1, row=8)

    
    def atualizar_paciente(self, cpf_atualizar, valor_mudanca, novo_valor):
        paciente_atualizado = self.menu.atualizar_paciente(cpf_atualizar, valor_mudanca, novo_valor)
        self.tela_atualiza_paciente.destroy()
        messagebox.showinfo("Paciente atualizado!", f"CPF: {paciente_atualizado.cpf} \n{valor_mudanca}: {novo_valor}")

    def criar_tela_atualiza_medico(self):
        self.tela_atualiza_medico = ttk.Frame(self.janela_principal, padding="10")
        self.tela_atualiza_medico.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.valor_mudanca_medico = tk.StringVar()
        self.escolher_mudanca_medico = ttk.Radiobutton(self.tela_atualiza_medico, text="Nome", variable=self.valor_mudanca_medico, value="Nome")
        self.escolher_mudanca_medico.grid(column=1, row=1)
        self.escolher_mudanca_medico = ttk.Radiobutton(self.tela_atualiza_medico, text="CRM", variable=self.valor_mudanca_medico, value="CRM")
        self.escolher_mudanca_medico.grid(column=2, row=1)
        self.escolher_mudanca_medico = ttk.Radiobutton(self.tela_atualiza_medico, text="Senha", variable=self.valor_mudanca_medico, value="Senha")
        self.escolher_mudanca_medico.grid(column=3, row=1)

        ttk.Label(self.tela_atualiza_medico, text="CRM do médico a ser atualizado:").grid(column=0, row=0, sticky=tk.W)
        self.crm_atualizar = ttk.Entry(self.tela_atualiza_medico)
        self.crm_atualizar.grid(column=1, row=0)

        ttk.Button(self.tela_atualiza_medico, text="Próximo", command=self.coletar_informacoes_atualiza_medico).grid(column=1, row=6)


    def coletar_informacoes_atualiza_medico(self):
        crm_atualizar = self.crm_atualizar.get()
        valor_mudanca_medico = self.valor_mudanca_medico.get()

        if valor_mudanca_medico == "Nome":
            ttk.Label(self.tela_atualiza_medico, text="Novo nome").grid(column=0, row=7, sticky=tk.W)
            self.novo_nome_medico = ttk.Entry(self.tela_atualiza_medico)
            self.novo_nome_medico.grid(column=1, row=7)
            ttk.Button(self.tela_atualiza_medico, text="Atualizar", command=lambda: self.atualizar_medico(crm_atualizar, valor_mudanca_medico, self.novo_nome_medico.get())).grid(column=1, row=8)

        elif valor_mudanca_medico == "CRM":
            ttk.Label(self.tela_atualiza_medico, text="Novo CRM").grid(column=0, row=7, sticky=tk.W)
            self.novo_crm = ttk.Entry(self.tela_atualiza_medico)
            self.novo_crm.grid(column=1, row=7)
            ttk.Button(self.tela_atualiza_medico, text="Atualizar", command=lambda: self.atualizar_medico(crm_atualizar, valor_mudanca_medico, self.novo_crm.get())).grid(column=1, row=8)

        elif valor_mudanca_medico == "Senha":
            ttk.Label(self.tela_atualiza_medico, text="Nova idade:").grid(column=0, row=7, sticky=tk.W)
            self.nova_senha_medico = ttk.Entry(self.tela_atualiza_medico)
            self.nova_senha_medico.grid(column=1, row=7)
            ttk.Button(self.tela_atualiza_medico, text="Atualizar", command=lambda: self.atualizar_medico(crm_atualizar, valor_mudanca_medico, self.nova_senha_medico.get())).grid(column=1, row=8)


    def atualizar_medico(self, crm_atualizar, valor_mudanca_medico, novo_valor):
        medico_atualizado = self.menu.atualizar_medico(crm_atualizar, valor_mudanca_medico, novo_valor)
        self.tela_atualiza_medico.destroy()
        messagebox.showinfo("Médico atualizado!", f"CRM: {medico_atualizado.crm} \n{valor_mudanca_medico}: {novo_valor}")
    
    def ver_todas_contas(self):
            lista_pacientes = '\n'.join([f"Nome: {p.nome}, Senha codificada: {p.senha_codificada}, CPF: {p.cpf}" for p in self.menu.lista_pacientes])
            messagebox.showinfo("Contas de pacientes", lista_pacientes)
            lista_medicos = '\n'.join([f"Nome: {m.nome}, Senha codificada: {m.senha_codificada}, CRM: {m.crm}" for m in self.menu.lista_medicos])
            messagebox.showinfo("Contas de médicos", lista_medicos)

    def processar_opcao(self, opcao):
        
        if opcao == "1- Cadastrar um paciente":
            self.criar_tela_cadastro_paciente()

        if opcao == "2- Cadastrar um médico":
            self.criar_tela_cadastro_medico()

        if opcao == "3- Atualizar informações de algum paciente já cadastrado":
            self.criar_tela_atualiza_paciente()
            
        if opcao == "4- Atualizar informações de algum médico já cadastrado":
            self.criar_tela_atualiza_medico()

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
        
        if opcao == "10- Ver pacientes cadastrados":
            self.ver_todas_contas()
