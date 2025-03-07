import pygame
from tkinter import *
from tkinter import ttk
import os
from os import listdir
from os.path import isfile, join
import webbrowser, os
import shutil
from tkinter.filedialog import askdirectory, askopenfilenames
from tkinter.messagebox import askyesnocancel

# caminho ="C:/Users\PEDROGUILHERMEFERRAR\Downloads"
# webbrowser.open(os.path.realpath(caminho))

pygame.mixer.init()
caminho = 'musicas'


janela = Tk()

class FuncoesBotoes():
   
    def carregar_musicas(self):
        # Carrega os arquivos de música para a biblioteca
        for f in listdir (caminho):
            if isfile(join(caminho, f)):
                self.biblioteca_musicas.append(f)

  
    def tocar_musica(self):
        print("Tocando música")
        musica_selecionada = self.lista_musicas.selection()
        if musica_selecionada:
            musica = self.lista_musicas.item(musica_selecionada[0])['values'][0]
            print(f"Tocando {musica}")
            self.tocar_audio(join(caminho, musica))

    def tocar_audio(self, musica):
        # Carrega e toca a música com pygame
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play()

    def parar_musica(self):
        # Para a música em execução
        pygame.mixer.music.stop()

    def pausar_musica(self):
        # Pausa a música
        pygame.mixer.music.pause()

    def retomar_musica(self):
        # Retoma a música que foi pausada
        pygame.mixer.music.unpause()

    def atualizar_lista(self):
        # Limpa a Treeview antes de adicionar os novos dados
        self.lista_musicas.delete(*self.lista_musicas.get_children())
        
        # Insere os novos dados da lista de músicas
        for musica in self.biblioteca_musicas:
            self.lista_musicas.insert("", "end", values=(musica,))

    def adicionar_musica(self):
        #caminho ="C:\\Users\PEDROGUILHERMEFERRAR\\Desktop"
        downloads = "C:\\Users\\GregórioDeAlmeidaQue\\Desktop\\PROJETOS\\Grupo6_SPOTIPY\\musicas"
        #t = webbrowser.open(os.path.realpath(caminho))
        #path = os.path.realpath(caminho)
        #os.startfile(path)
        
        
        #shutil.copyfile(downloads,caminho)
        #shutil.copyfile(caminho, os.path.join(downloads,'musicas'))
        arquivo_de_musica = askopenfilenames(title="Selecione um arquivo de música no computador")
        print(arquivo_de_musica[0])
        shutil.copy2(arquivo_de_musica[0], downloads)
        nome_musica = arquivo_de_musica[0].split("/")[-1]
        self.biblioteca_musicas.append(nome_musica)
        self.atualizar_lista()
        print("COnsegui atualizar a lista?")


        

    def deletar_musica(self):
        # Lógica para deletar uma música (baseado na seleção ou índice)
        selecionado = self.lista_musicas.selection()
        if selecionado:
            musica_selecionada = self.lista_musicas.item(selecionado[0])['values'][0]
            # Deleta o arquivo da música
            try:
                os.remove(join(caminho, musica_selecionada))
                print(f"Música {musica_selecionada} deletada.")
                # Atualiza a lista
                self.atualizar_lista()
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            except Exception as e:
                print(f"Erro ao tentar deletar a música: {e}")

    def proxima_musica(self):
        qtd_musicas = len(self.biblioteca_musicas)
        indice_proxima_musica = 0
        selecionado = self.lista_musicas.selection()  # Obtém os itens selecionados

        if selecionado:
            # Pega o ID do item selecionado e extrai o nome da música
            musica_selecionada = self.lista_musicas.item(selecionado[0])['values'][0]
            # Encontra o índice da música na lista de músicas
            indice_musica_atual = self.biblioteca_musicas.index(musica_selecionada)
            
            # Calcula o índice da próxima música, com loop se for o final da lista
            if indice_musica_atual >= qtd_musicas - 1:
                indice_proxima_musica = 0
            else:
                indice_proxima_musica = indice_musica_atual + 1

            # Seleciona a próxima música no Treeview
            musica_proxima = self.biblioteca_musicas[indice_proxima_musica]
            
            # Encontra o item correspondente à próxima música e seleciona no TreeView
            for item in self.lista_musicas.get_children():
                if self.lista_musicas.item(item)['values'][0] == musica_proxima:
                    self.lista_musicas.selection_set(item)
                    self.lista_musicas.focus(item)  # Coloca o foco na próxima música
                    break

            print(f"Índice da próxima música: {indice_proxima_musica}")
            self.tocar_musica()
            

        else:
            print("Nenhuma música selecionada")

    def musica_anterior(self):
        qtd_musicas = len(self.biblioteca_musicas)
        indice_anterior_musica = 0

        selecionado = self.lista_musicas.selection() 

        if selecionado:
            musica_selecionada = self.lista_musicas.item(selecionado[0])['values'][0]
            indice_musica_atual = self.biblioteca_musicas.index(musica_selecionada)

            if indice_musica_atual >= qtd_musicas :
                indice_anterior_musica = 0
            else:
                indice_anterior_musica = indice_musica_atual - 1
        musica_anterior = self.biblioteca_musicas[indice_anterior_musica]
            
            # Encontra o item correspondente à próxima música e seleciona no TreeView
        for item in self.lista_musicas.get_children():
                if self.lista_musicas.item(item)['values'][0] == musica_anterior:
                    self.lista_musicas.selection_set(item)
                    self.lista_musicas.focus(item)  # Coloca o foco na próxima música
                    break

        print(f"Índice da música anterior: {indice_anterior_musica}")
        self.tocar_musica()
            

                



class PlayerSpotPY(FuncoesBotoes):
    def __init__(self):
        self.janela = janela
        self.biblioteca_musicas = []  # Inicializando o atributo biblioteca_musicas
        self.tela_geral()
        self.frames_da_tela()
        self.botoes_e_informacoes()
        self.carregar_musicas()  # Chama o método que carrega os dados da agenda
        self.lista_frame2()
        janela.mainloop()

    def tela_geral(self):
        self.janela.title("SPOTIPY")
        self.janela.configure(background="#00fa9a")
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=600, height=400)

    def frames_da_tela(self):
        self.frame0 = Frame(self.janela, bd=4, bg='#7cffc6', highlightbackground='#0e0e10', highlightthickness=3)
        self.frame0.place(relx=0.04, rely=0.02, relwidth=0.92, relheight=0.10)

        self.frame1 = Frame(self.janela, bd=4, bg='#7cffc6', highlightbackground='#0e0e10', highlightthickness=3)
        self.frame1.place(relx=0.04, rely=0.15, relwidth=0.92, relheight=0.10)

        self.frame2 = Frame(self.janela, bd=4, bg='#7cffc6', highlightbackground='#0e0e10', highlightthickness=3)
        self.frame2.place(relx=0.04, rely=0.28, relwidth=0.92, relheight=0.70)

    def botoes_e_informacoes(self):
        # Criando as entradas (input fields)
        self.label_titulo = Label(self.frame0, text="SPOTI", bg='#7cffc6', font=('verdana', '23', 'bold'), fg='#0e0e10')
        self.label_titulo.place(relx=0.39, rely=0.12)

        self.label_titulo = Label(self.frame0, text="PY", bg='#7cffc6', font=('verdana', '23', 'bold'), fg='#006400')
        self.label_titulo.place(relx=0.525, rely=0.12)

        self.label_desc = Label(self.frame1, text="ADICIONAR NOVA MÚSICA", bg='#7cffc6', font=('verdana', '12', 'bold'), fg='#0e0e10')
        self.label_desc.place(relx=0.05, rely=0.12)
        
        # Criando os botões
        self.ad_confirmar = Button(self.frame1, text="PROCURAR", bg='#0e0e10', fg='#ffffff', font=('verdana', '8', 'bold'), command=self.adicionar_musica)
        self.ad_confirmar.place(relx=0.80, rely=0.05, relwidth=0.14, relheight=0.80)

        self.ad_tocar = Button(self.frame2, text="TOCAR", bg='#0e0e10', fg='#ffffff', font=('verdana', '8', 'bold'), command=self.tocar_musica)
        self.ad_tocar.place(relx=0.1, rely=0.85, relwidth=0.1, relheight=0.1)

        self.ad_pausar = Button(self.frame2, text="PAUSAR", bg='#0e0e10',fg='#ffffff', font=('verdana', '8', 'bold'), command=self.pausar_musica)
        self.ad_pausar.place(relx=0.45, rely=0.85, relwidth=0.1, relheight=0.1)
        
        self.ad_deletar = Button(self.frame2, text="DELETAR", bg='#0e0e10', fg='#ffffff', font=('verdana', '8', 'bold'), command=self.deletar_musica)
        self.ad_deletar.place(relx=0.80, rely=0.85, relwidth=0.1, relheight=0.1)

        self.ad_proxima_musica = Button(self.frame2, text=">|" ,font=('verdana', '8', 'bold'), command=self.proxima_musica) 
        self.ad_proxima_musica.place(relx=0.60, rely=0.85, relwidth=0.1, relheight=0.1)

        self.ad_musica_anterior = Button(self.frame2, text="|<" ,font=('verdana', '8', 'bold'), command=self.musica_anterior)
        self.ad_musica_anterior.place(relx=0.30, rely=0.85, relwidth=0.1, relheight=0.1)
    def lista_frame2(self):
        # Criando o Treeview
        self.lista_musicas = ttk.Treeview(self.frame2, height=100, columns=("col1", "col2", "col3", "col4"))
        self.lista_musicas.heading("#1", text="LISTA DE MÚSICAS")

        # Configurando as colunas
        self.lista_musicas.column("#0", width=0)
        self.lista_musicas.column("#1", width=500)

        # Inserindo os dados no Treeview
        for musica in self.biblioteca_musicas:
            self.lista_musicas.insert("", "end", values=(musica,))

        # Colocando o Treeview na tela
        self.lista_musicas.place(relx=0.04, rely=0.05, relwidth=0.92, relheight=0.7)


        # Criando a barra de rolagem
        self.scroll_lista = Scrollbar(self.frame2, orient='vertical', command=self.lista_musicas.yview)
        self.lista_musicas.configure(yscroll=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.96, rely=0.055, relwidth=0.02, relheight=0.693)

PlayerSpotPY()
