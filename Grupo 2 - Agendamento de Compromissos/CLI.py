import pandas as pd
import os

class FuncoesBotoes:
    def __init__(self):
        self.compromissos_agendados = []
        self.colunas_agenda = ["Descrição", "Horário", "Data", "Local"]

    def limpar_tela(self):
        print("\nCampos limpos!\n")

    def carregar_agenda(self, filename="agenda.xlsx"):
        if os.path.isfile(filename):
            tabela = pd.read_excel(filename)
            self.compromissos_agendados = tabela.values.tolist()
            print(f"\nAgenda carregada com sucesso: {len(self.compromissos_agendados)} compromissos encontrados.\n")
        else:
            print("\nArquivo de agenda não encontrado. Criando uma nova agenda...\n")

    def confirmar(self, dados):
        self.compromissos_agendados.append(dados)
        print("\nCompromisso adicionado com sucesso!")
        self.atualizar_lista()

    def atualizar_lista(self):
        df = pd.DataFrame(self.compromissos_agendados, columns=self.colunas_agenda)
        df.to_excel("agenda.xlsx", index=False)
        print("\nLista atualizada e salva no arquivo 'agenda.xlsx'!\n")
        self.listar_compromissos()

    def deletar_compromisso(self):
        self.listar_compromissos()
        if not self.compromissos_agendados:
            return
        try:
            indice = int(input("Digite o número do compromisso que deseja deletar: ")) - 1
            if 0 <= indice < len(self.compromissos_agendados):
                removido = self.compromissos_agendados.pop(indice)
                print(f"\nCompromisso '{removido[0]}' deletado com sucesso!")
                self.atualizar_lista()
            else:
                print("\nNúmero inválido.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    def editar_compromisso(self):
        self.listar_compromissos()
        if not self.compromissos_agendados:
            return
        try:
            indice = int(input("Digite o número do compromisso que deseja editar: ")) - 1
            if 0 <= indice < len(self.compromissos_agendados):
                compromisso = self.compromissos_agendados[indice]
                print(f"\nEditando compromisso: {compromisso}")
                descricao = input("Nova descrição (ou Enter para manter): ") or compromisso[0]
                horario = input("Novo horário (ou Enter para manter): ") or compromisso[1]
                data = input("Nova data (ou Enter para manter): ") or compromisso[2]
                local = input("Novo local (ou Enter para manter): ") or compromisso[3]

                self.compromissos_agendados[indice] = [descricao, horario, data, local]
                print("\nCompromisso editado com sucesso!")
                self.atualizar_lista()
            else:
                print("\nNúmero inválido.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    def listar_compromissos(self):
        if not self.compromissos_agendados:
            print("\nNenhum compromisso agendado.\n")
        else:
            print("\nCompromissos agendados:")
            print("=" * 50)
            for i, compromisso in enumerate(self.compromissos_agendados, start=1):
                print(f"{i}. {compromisso[0]} - {compromisso[1]} - {compromisso[2]} - {compromisso[3]}")
            print("=" * 50)

class AgendamentoDeReunioes(FuncoesBotoes):
    def __init__(self):
        super().__init__()
        self.carregar_agenda()
        self.menu()

    def menu(self):
        while True:
            print("\n=== MENU ===")
            print("1. Listar compromissos")
            print("2. Adicionar compromisso")
            print("3. Editar compromisso")
            print("4. Deletar compromisso")
            print("5. Sair")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.listar_compromissos()
                elif opcao == 2:
                    descricao = input("Descrição: ")
                    horario = input("Horário: ")
                    data = input("Data: ")
                    local = input("Local: ")
                    self.confirmar([descricao, horario, data, local])
                elif opcao == 3:
                    self.editar_compromisso()
                elif opcao == 4:
                    self.deletar_compromisso()
                elif opcao == 5:
                    print("\nSaindo...")
                    break
                else:
                    print("\nOpção inválida. Tente novamente.")
            except ValueError:
                print("\nEntrada inválida. Digite um número.")

# Executar o programa
if __name__ == "__main__":
    AgendamentoDeReunioes()