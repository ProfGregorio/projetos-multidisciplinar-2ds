from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import pandas as pd
import os

arquivo_existe = os.path.isfile('agenda.xlsx')

janela = Tk()

# Criei uma classe para colocar as configurações de cada botão para definir o que cada um vai fazer
class FuncoesBotoes():
    def limpar_tela(self):
        self.entry_desc.delete(0, END)
        self.entry_hora.delete(0, END)
        self.entry_loc.delete(0, END)
        self.entry_cal.delete(0, END)
    
    def carregar_agenda(self, filename="agenda.xlsx"):
        # Lê o arquivo Excel
        tabela = pd.read_excel(filename)
        self.compromissos_agendados = tabela.values.tolist()
        self.colunas_agenda = tabela.columns.values
        
    def confirmar(self, dados):
        self.compromissos_agendados.append(dados)
        self.limpar_tela()
        self.atualizar_lista()  # Atualiza a Treeview

    def atualizar_lista(self):
        df = pd.DataFrame(self.compromissos_agendados, columns=self.colunas_agenda)
        df.to_excel("agenda.xlsx",  index=False)
                
        # Limpa a Treeview antes de adicionar os novos dados
        for item in self.lista_compromisso.get_children():
            self.lista_compromisso.delete(item)

        # Insere os novos dados da lista de compromissos
        for compromisso in self.compromissos_agendados:
            self.lista_compromisso.insert("", "end", values=compromisso)

    def deletar_compromisso(self):
        # Lógica para deletar um compromisso (baseado na seleção ou índice)
        item_selecionado = self.lista_compromisso.selection()
        if item_selecionado:
            # Aqui você pode remover da lista de compromissos a partir do índice ou valores
            for item in item_selecionado:
                valores_item = self.lista_compromisso.item(item, "values")
                self.compromissos_agendados = [comp for comp in self.compromissos_agendados if comp != list(valores_item)]

            # Atualiza a Treeview após deletar
            self.atualizar_lista()

    def editar_compromisso(self):
            # Lógica para editar um compromisso da lista de compromissos a partir do índice ou valores
            item_selecionado = self.lista_compromisso.selection()
            if item_selecionado:
                 #Aqui você pode editar um compromisso da lista de compromissos a partir do índice ou valores
                 for item in item_selecionado:
                     valores_item = self.lista_compromisso.item(item, "values")
                     self.entry_desc.insert(0,valores_item[0])
                     self.entry_hora.insert(0,valores_item[1])
                     self.entry_cal.insert(0,valores_item[2])
                     self.entry_loc.insert(0,valores_item[3])
                     self.compromissos_agendados = [comp for comp in self.compromissos_agendados if comp != list(valores_item)]

                 self.atualizar_lista()

    def abrir_calendario(self):
        calendario = Tk()
        calendario.title("Calendário")
        calendario.geometry("300x300")
        cal = Calendar(calendario, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
        cal.pack(pady = 20, padx = 25)
 
        def grad_date():
            date_ = cal.get_date()
            if (date_[2] == "/"):
                mes = date_[:2]
            else:
                mes = date_[:1]
            if (date_[len(mes)+2] == "/"):
                dia = date_[len(mes)+1:len(mes)+2]
            else: 
                dia = date_[len(mes)+1:len(mes)+3]
            ano = date_[-2:]
            date.config(text = "Selected Date is: " + cal.get_date())
            data_v = dia+"/"+mes+"/"+ano
            self.entry_cal.insert(0, data_v)
            calendario.destroy()

        Button(calendario, text = "Selecionar data",
        command = grad_date).pack(pady = 20)
            
        date = Label(calendario, text = "")

        date.pack(pady = 20)

        calendario.mainloop()
            
# Criei uma classe para colocar as configurações e funcionalidades da janela aonde vamos colocar as informações do agendamento
class AgendamentoDeReunioes(FuncoesBotoes):
    def __init__(self):
        self.janela = janela
        self.compromissos_agendados = []  # Inicializando o atributo compromissos_agendados
        self.colunas_agenda = []  # Inicializando o atributo colunas_agenda
        self.tela_geral()
        self.frames_da_tela()
        self.botoes_e_informacoes()
        self.carregar_agenda()  # Chama o método que carrega os dados da agenda
        self.lista_frame2()
        janela.mainloop()

    def tela_geral(self):
        self.janela.title("Agendamento de Compromissos - Excel")
        self.janela.configure(background="#9ebae6")
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=600, height=400)

    def frames_da_tela(self):
        self.frame1 = Frame(self.janela, bd=4, bg='#60a1bf', highlightbackground='#4a7d8c', highlightthickness=3)
        self.frame1.place(relx=0.04, rely=0.05, relwidth=0.92, relheight=0.35)

        self.frame2 = Frame(self.janela, bd=4, bg='#60a1bf', highlightbackground='#4a7d8c', highlightthickness=3)
        self.frame2.place(relx=0.04, rely=0.45, relwidth=0.92, relheight=0.35)

    def botoes_e_informacoes(self):
        # Criando os botões
        self.ad_confirmar = Button(self.frame1, text="CONFIRMAR", bg='#4a7487', fg='#ffffff', font=('verdana', '8', 'bold'), command=lambda: self.confirmar([self.entry_desc.get(), self.entry_hora.get(), self.entry_cal.get(), self.entry_loc.get()]))

        self.ad_confirmar.place(relx=0.8, rely=0.8, relwidth=0.14, relheight=0.13)

        self.ad_limpar = Button(self.frame1, text="LIMPAR", bg='#4a7487', fg='#ffffff', font=('verdana', '8', 'bold'), command=self.limpar_tela)
        self.ad_limpar.place(relx=0.615, rely=0.8, relwidth=0.1, relheight=0.13)

        self.ad_deletar = Button(self.frame2, text="DELETAR", bg='#a31717', font=('verdana', '8', 'bold'), command=self.deletar_compromisso)
        self.ad_deletar.place(relx=0.87, rely=0.1, relwidth=0.1, relheight=0.13)

        self.ad_editar = Button(self.frame2, text="EDITAR", bg='#4a7487', fg='#ffffff', font=('verdana', '8', 'bold'), command=self.editar_compromisso)
        self.ad_editar.place(relx=0.67, rely=0.1, relwidth=0.1, relheight=0.13)

        self.ad_calendario = Button(self.frame1, text="SELECIONAR", bg='#4a7487', fg='#ffffff', font=('verdana', '8', 'bold'), command=self.abrir_calendario)
        self.ad_calendario.place(relx=0.8, rely=0.4, relwidth=0.14, relheight=0.13)

        # Criando as entradas (input fields)
        self.label_desc = Label(self.frame1, text="DESCRIÇÃO DO COMPROMISSO", bg='#60a1bf', font=('verdana', '10', 'bold'), fg='#4a7487')
        self.label_desc.place(relx=0.11, rely=0.05)


        self.entry_desc = Entry(self.frame1)
        self.entry_desc.place(relx=0.043, rely=0.2, relwidth=0.5)

        self.label_hora = Label(self.frame1, text="HORÁRIO", bg='#60a1bf', font=('verdana', '10', 'bold'), fg='#4a7487')
        self.label_hora.place(relx=0.61, rely=0.05)

        self.entry_hora = Entry(self.frame1)
        self.entry_hora.place(relx=0.62, rely=0.2, relwidth=0.09)

        self.label_data = Label(self.frame1, text="DATA", bg='#60a1bf', font=('verdana', '10', 'bold'), fg='#4a7487')
        self.label_data.place(relx=0.83, rely=0.05)

        self.label_loc = Label(self.frame1, text="LOCALIZAÇÃO DO COMPROMISSO", bg='#60a1bf', font=('verdana', '10', 'bold'), fg='#4a7487')
        self.label_loc.place(relx=0.11, rely=0.35)

        self.entry_loc = Entry(self.frame1)
        self.entry_loc.place(relx=0.043, rely=0.53, relwidth=0.5)

        self.entry_cal = Entry(self.frame1, text= "", font=('verdana', '10', 'bold'), fg='#4a7487')
        self.entry_cal.place(relx=0.8, rely=0.20, relwidth=0.14)

    def lista_frame2(self):
        # Criando o Treeview
        self.lista_compromisso = ttk.Treeview(self.frame2, height=10, columns=("col1", "col2", "col3", "col4"))
        self.lista_compromisso.heading("#1", text="DESCRIÇÃO")
        self.lista_compromisso.heading("#2", text="HORÁRIO")
        self.lista_compromisso.heading("#3", text="DATA")        
        self.lista_compromisso.heading("#4", text="LOCALIZAÇÃO")

        # Configurando as colunas
        self.lista_compromisso.column("#0", width=0)
        self.lista_compromisso.column("#1", width=150)
        self.lista_compromisso.column("#2", width=100)
        self.lista_compromisso.column("#3", width=100)
        self.lista_compromisso.column("#4", width=150)

        # Inserindo os dados no Treeview
        for compromisso in self.compromissos_agendados:
            print(compromisso)
            self.lista_compromisso.insert("", "end", values=compromisso)

        # Colocando o Treeview na tela
        self.lista_compromisso.place(relx=0.04, rely=0.29, relwidth=0.92, relheight=0.61)

        # Criando a barra de rolagem
        self.scroll_lista = Scrollbar(self.frame2, orient='vertical', command=self.lista_compromisso.yview)
        self.lista_compromisso.configure(yscroll=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.96, rely=0.3, relwidth=0.02, relheight=0.594)

# Executando a classe principal
AgendamentoDeReunioes()
