import tkinter as tk
import json
from tkinter import ttk, messagebox
from menu import Menu
from pessoa import Pessoa

class App():
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema Hospitalar")
        self.menu = Menu()

    def criar_tela_menu(self):
        self.limpar_tela()
        tk.Label(self.master, text="Sistema Hospitalar", font=("Helvetica", 16)).pack(pady=20)

        opcoes = self.menu.mostrar_opcoes()
        for i, opcao in enumerate(opcoes):
            tk.Button(self.master, text=opcao, command=lambda o=opcao: self.processar_opcao(o)).pack(pady=10)

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
            self.verificar_consultas()
            
        if opcao == "7- Remarcar consultas":
            self.remarcar_consulta()
            
        if opcao == "8- Cancelar consultas":
            self.cancelar_consulta()
        
        if opcao == "9- Ver pacientes cadastrados":
            self.ver_todas_contas() 

    def limpar_tela(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def criar_tela_cadastro_paciente(self):
        self.limpar_tela()
        tk.Label(self.master, text="Cadastrar Paciente", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Nome:").pack()
        self.nome = tk.Entry(self.master)
        self.nome.pack()
        tk.Label(self.master, text="Senha:").pack()
        self.senha = tk.Entry(self.master, show="*")
        self.senha.pack()
        tk.Label(self.master, text="CPF:").pack()
        self.cpf = tk.Entry(self.master)
        self.cpf.pack()

        tk.Button(self.master, text="Cadastrar", command=self.coletar_informacoes_paciente).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()
  
    def coletar_informacoes_paciente(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        senha = self.senha.get()

        try:
            with open('dados_pacientes.json', 'r') as file:
                dados = json.load(file)
                if not self.menu.verifica_cpf(cpf):
                    messagebox.showerror("Erro", "CPF inválido")
                elif cpf in dados.get('cpfs', []):
                    messagebox.showerror("Erro","CPF já está em uso. Por favor, digite um CPF diferente.")
                elif len(senha) < 8:
                    messagebox.showerror("Erro","Senha inválida, mínimo de 8 dígitos" )
                else:
                    paciente = self.menu.cadastrar_paciente(nome, senha, cpf)
                    self.limpar_tela()
                    messagebox.showinfo("Paciente cadastrado!", f"Nome: {paciente.nome} \nSenha: {paciente.senha_codificada}\nCPF: {paciente.cpf}")
                    self.criar_tela_menu()
        except FileNotFoundError:
            dados = { 'pacientes': [], 'cpfs': []}
            if not self.menu.verifica_cpf(cpf):
                messagebox.showerror("Erro", "CPF inválido")
            elif len(senha) < 8:
                messagebox.showerror("Erro","Senha inválida, mínimo de 8 dígitos" )
            else:
                paciente = self.menu.cadastrar_paciente(nome, senha, cpf)
                dados['cpfs'].append(cpf)
                dados['pacientes'].append(paciente.descricao())
                with open('dados_pacientes.json', 'w') as file:
                    json.dump(dados, file, indent=4)
                self.limpar_tela()
                messagebox.showinfo("Paciente cadastrado!", f"Nome: {paciente.nome} \nSenha: {paciente.senha_codificada}\nCPF: {paciente.cpf}")
                self.criar_tela_menu()

    def criar_tela_cadastro_medico(self):
        self.limpar_tela()
        tk.Label(self.master, text="Cadastrar Médico", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Nome:").pack()
        self.nome = tk.Entry(self.master)
        self.nome.pack()
        tk.Label(self.master, text="Senha:").pack()
        self.senha = tk.Entry(self.master, show="*")
        self.senha.pack()
        tk.Label(self.master, text="CRM:").pack()
        self.crm = tk.Entry(self.master)
        self.crm.pack()

        self.valor_especializacao = tk.StringVar()
        tk.Label(self.master, text="Especialização:").pack()
        self.especializacao_ortopedia = ttk.Radiobutton(self.master, text="Ortopedia", variable=self.valor_especializacao, value="Ortopedia")
        self.especializacao_ortopedia.pack()
        self.especializacao_pediatria = ttk.Radiobutton(self.master, text="Pediatria", variable=self.valor_especializacao, value="Pediatria")
        self.especializacao_pediatria.pack()
        self.especializacao_cardiologia = ttk.Radiobutton(self.master, text="Cardiologia", variable=self.valor_especializacao, value="Cardiologia")
        self.especializacao_cardiologia.pack()
        self.especializacao_dermatologia = ttk.Radiobutton(self.master, text="Dermatologia", variable=self.valor_especializacao, value="Dermatologia")
        self.especializacao_dermatologia.pack()
        self.especializacao_endocrinologia = ttk.Radiobutton(self.master, text="Endocrinologia", variable=self.valor_especializacao, value="Endocrinologia")
        self.especializacao_endocrinologia.pack()

        tk.Button(self.master, text="Cadastrar", command= self.coletar_informacoes_medico).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def coletar_informacoes_medico(self):
        nome = self.nome.get()
        senha = self.senha.get()
        crm = self.crm.get()
        especializacao = self.valor_especializacao.get()

        try:
            with open('dados_medicos.json', 'r') as file:
                dados = json.load(file)
                if len(crm) != 9:
                    messagebox.showerror("Erro", "CRM inválido, deve ter 9 dígitos")
                elif crm in dados.get('crms', []):
                    messagebox.showerror("Erro","CRM já está em uso. Por favor, digite um CPF diferente.")
                elif len(senha) < 8:
                    messagebox.showerror("Erro","Senha inválida, mínimo de 8 dígitos" )
                else:
                    medico = self.menu.cadastrar_medico(nome, senha, crm, especializacao)
                    self.limpar_tela()
                    messagebox.showinfo("Médico cadastrado!", f"Nome: {medico.nome} \nSenha: {medico.senha_codificada} \nCRM: {medico.crm}  \nEspecialização: {medico.especializacao}")
                    self.criar_tela_menu()
        except FileNotFoundError:
            dados = {'medicos': [], 'crms': []}
            if len(crm) != 9:
                    messagebox.showerror("Erro", "CRM inválido, deve ter 9 dígitos")
            elif len(senha) < 8:
                    messagebox.showerror("Erro","Senha inválida, mínimo de 8 dígitos" )
            else:
                medico = self.menu.cadastrar_medico(nome, senha, crm, especializacao)
                dados['crms'].append(crm)
                dados['medicos'].append(medico.descricao())
                with open('dados_medicos.json', 'w') as file:
                    json.dump(dados, file, indent=4)
                self.limpar_tela()
                messagebox.showinfo("Médico cadastrado!", f"Nome: {medico.nome} \nSenha: {medico.senha_codificada} \nCRM: {medico.crm}  \nEspecialização: {medico.especializacao}")
                self.criar_tela_menu()

    def criar_tela_atualiza_paciente(self):
        self.limpar_tela()
        tk.Label(self.master, text="Atualizar Informações do Paciente", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="CPF do Paciente:").pack()
        self.cpf_paciente = tk.Entry(self.master)
        self.cpf_paciente.pack()

        tk.Button(self.master, text="Buscar", command=self.buscar_paciente).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def buscar_paciente(self):
        cpf = self.cpf_paciente.get()
        with open('dados_pacientes.json', 'r') as file:
            dados = json.load(file)
            if cpf not in dados.get('cpfs', []):
                messagebox.showerror("Erro", "CPF não encontrado")
            else:
                self.criar_tela_atualiza_detalhes_paciente(cpf)
    
    def criar_tela_atualiza_detalhes_paciente(self, cpf):
        self.limpar_tela()
        tk.Label(self.master, text="Atualizar Informações do Paciente", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Novo Nome:").pack()
        self.nome = tk.Entry(self.master)
        self.nome.pack()
        tk.Label(self.master, text="Nova Senha:").pack()
        self.senha = tk.Entry(self.master, show="*")
        self.senha.pack()

        tk.Button(self.master, text="Atualizar", command=lambda: self.atualizar_paciente(cpf)).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def atualizar_paciente(self, cpf):
        nome = self.nome.get()
        senha = self.senha.get()
        
        with open('dados_pacientes.json', 'r') as file:
            dados = json.load(file)
        
        if not nome or not senha:
            messagebox.showerror("Erro", "Nome e senha não podem estar vazios")
        elif len(senha) < 8:
            messagebox.showerror("Erro", "Senha inválida, mínimo de 8 dígitos")
        else:
            for paciente in dados['pacientes']:
                if paciente['cpf'] == cpf:
                    paciente['nome'] = nome
                    pessoa = Pessoa(nome, senha) 
                    paciente['senha'] = pessoa.codifica_senha(senha)  
                    break
            
            with open('dados_pacientes.json', 'w') as file:
                json.dump(dados, file, indent=4)
            
            messagebox.showinfo("Atualização", "Informações do paciente atualizadas com sucesso")
            self.criar_tela_menu()

    def criar_tela_atualiza_medico(self):
        self.limpar_tela()
        tk.Label(self.master, text="Atualizar Informações do Médico", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="CRM do Médico:").pack()
        self.crm_medico = tk.Entry(self.master)
        self.crm_medico.pack()

        tk.Button(self.master, text="Buscar", command=self.buscar_medico).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def buscar_medico(self):
        crm = self.crm_medico.get()
        with open('dados_medicos.json', 'r') as file:
            dados = json.load(file)
            if crm not in dados.get('crms', []):
                messagebox.showerror("Erro", "CRM não encontrado")
            else:
                self.criar_tela_atualiza_detalhes_medico(crm)

    def criar_tela_atualiza_detalhes_medico(self, crm):
        self.limpar_tela()
        tk.Label(self.master, text="Atualizar Informações do Médico", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Novo Nome:").pack()
        self.nome = tk.Entry(self.master)
        self.nome.pack()
        tk.Label(self.master, text="Nova Senha:").pack()
        self.senha = tk.Entry(self.master, show="*")
        self.senha.pack()
        
        self.valor_especializacao = tk.StringVar()
        tk.Label(self.master, text="Especialização:").pack()
        self.especializacao_ortopedia = ttk.Radiobutton(self.master, text="Ortopedia", variable=self.valor_especializacao, value="Ortopedia")
        self.especializacao_ortopedia.pack()
        self.especializacao_pediatria = ttk.Radiobutton(self.master, text="Pediatria", variable=self.valor_especializacao, value="Pediatria")
        self.especializacao_pediatria.pack()
        self.especializacao_cardiologia = ttk.Radiobutton(self.master, text="Cardiologia", variable=self.valor_especializacao, value="Cardiologia")
        self.especializacao_cardiologia.pack()
        self.especializacao_dermatologia = ttk.Radiobutton(self.master, text="Dermatologia", variable=self.valor_especializacao, value="Dermatologia")
        self.especializacao_dermatologia.pack()
        self.especializacao_endocrinologia = ttk.Radiobutton(self.master, text="Endocrinologia", variable=self.valor_especializacao, value="Endocrinologia")
        self.especializacao_endocrinologia.pack()

        tk.Button(self.master, text="Atualizar", command=lambda: self.atualizar_medico(crm)).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def atualizar_medico(self, crm):
        nome = self.nome.get()
        senha = self.senha.get()
        especializacao = self.valor_especializacao.get()

        with open('dados_medicos.json', 'r') as file:
            dados = json.load(file)
        
        if not nome or not senha or not especializacao:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
        elif len(senha) < 8:
            messagebox.showerror("Erro", "Senha inválida, mínimo de 8 dígitos")
        else:
            for medico in dados['medicos']:
                if medico['CRM'] == crm:
                    medico['nome'] = nome
                    pessoa = Pessoa(nome, senha)
                    medico['senha'] = pessoa.codifica_senha(senha)
                    medico['Especialização'] = especializacao
                    break
            
            with open('dados_medicos.json', 'w') as file:
                json.dump(dados, file, indent=4)
            
            messagebox.showinfo("Atualização", "Informações do médico atualizadas com sucesso")
            self.criar_tela_menu()

    def agendar_consulta(self):
        self.limpar_tela()
        tk.Label(self.master, text="Agendar Consulta", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="CPF do Paciente:").pack()
        cpf_paciente = tk.Entry(self.master)
        cpf_paciente.pack()
        tk.Label(self.master, text="Especialização:").pack()
        especializacao = tk.Entry(self.master)
        especializacao.pack()
        tk.Label(self.master, text="Nome do Médico:").pack()
        nome_medico = tk.Entry(self.master)
        nome_medico.pack()
        tk.Label(self.master, text="Horário (HH:00):").pack()
        horario = tk.Entry(self.master)
        horario.pack()
        tk.Button(self.master, text="Agendar", command=lambda: self.realizar_agendamento(cpf_paciente.get(), especializacao.get(), nome_medico.get(), horario.get())).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def realizar_agendamento(self, cpf_paciente, especializacao, nome_medico, horario):
        resultado = self.menu.agendar_consulta_interface(cpf_paciente, especializacao, nome_medico, horario)
        if resultado:
            messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
            self.criar_tela_menu()
        else:
            messagebox.showerror("Erro", "Não foi possível agendar a consulta. Verifique os dados e tente novamente.")

    def verificar_consultas(self):
        self.limpar_tela()
        tk.Label(self.master, text="Verificar Consultas Agendadas", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Nome do Paciente:").pack()
        nome_paciente = tk.Entry(self.master)
        nome_paciente.pack()
        tk.Button(self.master, text="Verificar", command=lambda: self.exibir_consultas_agendadas(nome_paciente.get())).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def exibir_consultas_agendadas(self, nome_paciente):
        consultas = self.menu.verificar_consulta(nome_paciente)
        if consultas:
            self.limpar_tela()
            tk.Label(self.master, text=f"Consultas Agendadas para {nome_paciente}", font=("Helvetica", 14)).pack(pady=20)
            for consulta in consultas:
                tk.Label(self.master, text=f"Médico: {consulta['nome_medico']}, Horário: {consulta['horario']}").pack()
            tk.Button(self.master, text="Voltar", command=self.verificar_consultas).pack(pady=20)
            self.criar_tela_menu()
        else:
            messagebox.showinfo("Nenhuma Consulta", f"Nenhuma consulta agendada para {nome_paciente}")

    def remarcar_consulta(self):
        self.limpar_tela()
        tk.Label(self.master, text="Remarcar Consulta", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Nome do Paciente:").pack()
        nome_paciente = tk.Entry(self.master)
        nome_paciente.pack()
        tk.Label(self.master, text="Nome do Médico:").pack()
        nome_medico = tk.Entry(self.master)
        nome_medico.pack()
        tk.Label(self.master, text="Novo Horário (HH:00):").pack()
        novo_horario = tk.Entry(self.master)
        novo_horario.pack()
        tk.Button(self.master, text="Remarcar", command=lambda: self.realizar_remarcacao(nome_paciente.get(), nome_medico.get(), novo_horario.get())).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def realizar_remarcacao(self, nome_paciente, nome_medico, novo_horario):
        resultado = self.menu.editar_consulta_interface(nome_paciente, nome_medico, novo_horario)
        if resultado:
            messagebox.showinfo("Sucesso", "Consulta remarcada com sucesso!")
            self.criar_tela_menu()
        else:
            messagebox.showerror("Erro", "Não foi possível remarcar a consulta. Verifique os dados e tente novamente.")

    def cancelar_consulta(self):
        self.limpar_tela()
        tk.Label(self.master, text="Cancelar Consulta", font=("Helvetica", 14)).pack(pady=20)
        tk.Label(self.master, text="Nome do Paciente:").pack()
        nome_paciente = tk.Entry(self.master)
        nome_paciente.pack()
        tk.Button(self.master, text="Cancelar", command=lambda: self.realizar_cancelamento(nome_paciente.get())).pack(pady=20)
        tk.Button(self.master, text="Voltar", command=self.criar_tela_menu).pack()

    def realizar_cancelamento(self, nome_paciente):
        resultado = self.menu.remover_consulta_interface(nome_paciente)
        if resultado:
            messagebox.showinfo("Sucesso", "Consulta cancelada com sucesso!")
            self.criar_tela_menu()
        else:
            messagebox.showerror("Erro", "Não foi possível cancelar a consulta. Verifique os dados e tente novamente.")

    def ver_todas_contas(self):
            lista_pacientes = '\n'.join([f"Nome: {p.nome}, Senha codificada: {p.senha_codificada}, CPF: {p.cpf}" for p in self.menu.lista_pacientes])
            messagebox.showinfo("Contas de pacientes", lista_pacientes)
            lista_medicos = '\n'.join([f"Nome: {m.nome}, Senha codificada: {m.senha_codificada}, CRM: {m.crm}" for m in self.menu.lista_medicos])
            messagebox.showinfo("Contas de médicos", lista_medicos)
