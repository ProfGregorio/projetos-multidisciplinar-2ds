from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self, master=None):        
        
        self.fontePadrao = ("Arial", "10")        
        self.primeiroContainer = Frame(master,  background="green", borderwidth=10, highlightcolor="yellow")
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master, background="red")
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack(side="left", fill="both", expand=True)

#        self.segundoContainer.pack()


        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="SPOTIPY")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Lista de Músicas", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        
        
        self.autenticar = Button(self.segundoContainer)
        self.autenticar["text"] = "Adicionar nova música"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 50
        self.autenticar["command"] = self.adicionarNovaMusica
        self.autenticar.pack()


        # self.nome = Entry(self.segundoContainer)
        # self.nome["width"] = 30
        # self.nome["font"] = self.fontePadrao
        # self.nome.pack(side=LEFT)
        

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.sair = Button(self.quartoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = self.sairSistema
        self.sair.pack()

        #ttk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=0)

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def adicionarNovaMusica(self):
        pass

    def sairSistema(self):
        root.destroy()


root = Tk()
root.title("SpotiPy")
root.configure(bg='green')
Application(root)
root.mainloop()


