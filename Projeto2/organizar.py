from pathlib import Path

def organizar_por_extensao(diretorio):
    try:
        path = Path(diretorio)
        if not path.is_dir():
            print("O diretório especificado não existe.")
            return

        arquivos = list(path.glob("*.txt*"))  # Pega todos os arquivos com extensão
        if not arquivos:
            print("Nenhum arquivo encontrado para organizar.")
            return

        for arquivo in arquivos:
            # Pega a extensão do arquivo
            extensao = arquivo.suffix[1:]  # Remove o ponto (.)
            subpasta = path / extensao

            # Cria a subpasta se não existir
            subpasta.mkdir(exist_ok=True)

            # Move o arquivo para a subpasta
            novo_caminho = subpasta / arquivo.name
            arquivo.rename(novo_caminho)
            print(f"Movido: {arquivo.name} -> {novo_caminho}")

        print("Organização por extensão concluída!")
    except Exception as e:
        print(f"Erro: {e}")

# Caso queira executar o Script individualmente
organizar_por_extensao(
    diretorio=r"C:\Users\jean0\Desktop\Projetos\Python\Projeto2\TESTES"  # Caminho
)
