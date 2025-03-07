from tkinter.filedialog import askdirectory, askopenfilenames
from tkinter.messagebox import askyesnocancel

arquivo_computador = askopenfilenames(title="Selecione um arquivo do computador")
print(arquivo_computador)

confirmacao = askyesnocancel(title="Confirmação", message="Você realmente quer iniciar essa automação?")
print(confirmacao)