import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self, items):
        super().__init__()

        # Armazenando os campos de entrada
        self.entry_fields = {}

        # Para cada item na lista, crie um label, um botão e um campo de entrada
        for index, item in enumerate(items):
            # Cria um label com o nome do item
            label = tk.Label(self, text=item)
            label.grid(row=index, column=0, padx=5, pady=5)

            # Cria um botão para copiar o nome do item
            copy_button = tk.Button(self, text="Copiar", command=lambda text=item: self.copy_text(text))
            copy_button.grid(row=index, column=1, padx=5, pady=5)

            # Cria um campo de entrada para exibir o nome copiado
            entry_field = tk.Entry(self)
            entry_field.grid(row=index, column=2, padx=5, pady=5)

            # Armazena o campo de entrada associado ao item
            self.entry_fields[item] = entry_field

    def copy_text(self, text):
        # Cola o texto no campo de entrada correspondente
        self.entry_fields[text].delete(0, tk.END)  # Limpa o campo antes de inserir
        self.entry_fields[text].insert(0, text)

if __name__ == "__main__":
    # Aqui você pegaria os itens do banco de dados, no exemplo é uma lista fixa
    items = ["Maçã", "Banana", "Grão de Bico", "Teste 1", "Teste 2", "Teste"]

    # Criação da janela principal
    window = MainWindow(items)
    window.title("Interface Dinâmica Tkinter")
    window.geometry("400x200")
    window.mainloop()
