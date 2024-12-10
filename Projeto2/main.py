import tkinter as tk
from tkinter import filedialog, messagebox
from renomear import renomear_arquivos
from organizar import organizar_por_extensao

def selecionar_diretorio():
    """Abre uma janela para selecionar o diretório."""
    diretorio = filedialog.askdirectory()
    if diretorio:
        entrada_diretorio.delete(0, tk.END)
        entrada_diretorio.insert(0, diretorio)

def executar_renomear():
    """Executa a funcionalidade de renomear arquivos."""
    diretorio = entrada_diretorio.get()
    padrao = entrada_padrao.get()
    extensao = entrada_extensao.get()
    if not diretorio or not padrao or not extensao:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return
    renomear_arquivos(diretorio, padrao, extensao)
    messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

def executar_organizar():
    """Executa a funcionalidade de organizar por extensão."""
    diretorio = entrada_diretorio.get()
    if not diretorio:
        messagebox.showerror("Erro", "O campo do diretório deve ser preenchido!")
        return
    organizar_por_extensao(diretorio)
    messagebox.showinfo("Sucesso", "Arquivos organizados por extensão!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Automação de Arquivos")
janela.geometry("400x300")

# Diretório
tk.Label(janela, text="Diretório:").pack(pady=5)
entrada_diretorio = tk.Entry(janela, width=40)
entrada_diretorio.pack(pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_diretorio).pack(pady=5)

# Campos para renomear
tk.Label(janela, text="Padrão de Renomeação:").pack(pady=5)
entrada_padrao = tk.Entry(janela, width=40)
entrada_padrao.pack(pady=5)

tk.Label(janela, text="Extensão (EX: .txt):").pack(pady=5)
entrada_extensao = tk.Entry(janela, width=40)
entrada_extensao.pack(pady=5)

# Botões
tk.Button(janela, text="Renomear Arquivos", command=executar_renomear).pack(pady=5)
tk.Button(janela, text="Organizar por Extensão", command=executar_organizar).pack(pady=5)

# Inicia a interface
janela.mainloop()
