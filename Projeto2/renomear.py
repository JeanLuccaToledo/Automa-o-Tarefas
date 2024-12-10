import os
from pathlib import Path

def renomear_arquivos(diretorio, padrao, extensao):
    """"
     Args:
        diretorio (str): Caminho do diretório.
        padrao (str): Padrão para renomear os arquivos.
        extensao (str): Extensão dos arquivos a renomear (exemplo: .txt).
    """
    
    try:
        path = Path(diretorio)
        if not path.is_dir():
            print("O diretório especificado não existe.")
            return

        arquivos = list(path.glob(f"*{extensao}"))
        if not arquivos:
            print(f"Nenhum arquivo com a extensão '{extensao}' encontrado.")
            return

        for i, arquivo in enumerate(arquivos, 1):
            novo_nome = path / f"{padrao}_{i}{extensao}"
            arquivo.rename(novo_nome)
            print(f"Renomeado: {arquivo.name} -> {novo_nome.name}")

        print("Renomeação concluída!")
    except Exception as e:
        print(f"Erro: {e}")

renomear_arquivos(
    diretorio = r"\Users\jean0\Desktop\Projetos\Python\Projeto2\TESTES",           # Substitua pelo caminho correto
    padrao="correto",                                                              # O nome base que você quer
    extensao=".txt"                                                                # A extensão dos arquivos (exemplo: .txt)
)
