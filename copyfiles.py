import os
import shutil
import sys

# Esta aplicação permite copiar todos os ficheiros que se encontram em sub diretorios, de um diretorio base, para outro diretorio.
# Permite responder à forma como o moodle descarrega os trabalhos. Cada estudante um sub diretorio, o que nos obriga a ir copiar tudo um a um.
# com esta abordagem, além de copiarmos todos os ficheiros para um único diretorio, tb renomeia cada ficheiro com o nome do estudante.
# ATENÇÃO: aos nomes dos subdiretorios que podem ser alterados para o local indicado ou passar como parametro

#Fernando Cassola (maio 2025)

# Para correr basta: python copyFiles.py "C:\origem" "C:\destino"

def copiar_arquivos(origem, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    for root, dirs, files in os.walk(origem):
        for file in files:
            # Nome do subdiretório relativo à origem
            subdir_relativo = os.path.relpath(root, origem)
            nome_subdir_completo = os.path.basename(subdir_relativo)
            # Extrai parte antes do primeiro "_", se existir
            nome_subdir = nome_subdir_completo.split("_")[0] if "_" in nome_subdir_completo else nome_subdir_completo


            # Constrói novo nome com o subdiretório no nome do ficheiro
            base, extensao = os.path.splitext(file)
            novo_nome = f"{nome_subdir}_{base}{extensao}" if nome_subdir != '.' else file
            caminho_destino = os.path.join(destino, novo_nome)

            # Evita sobrescrever ficheiros com nomes duplicados
            contador = 1
            while os.path.exists(caminho_destino):
                novo_nome = f"{nome_subdir}_{base}_{contador}{extensao}"
                caminho_destino = os.path.join(destino, novo_nome)
                contador += 1

            caminho_origem = os.path.join(root, file)
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Copiado: {caminho_origem} -> {caminho_destino}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        origem = sys.argv[1]
        destino = sys.argv[2]
    else:
        origem = 'C:\\Projects\\aulas\\CopiarFicheirosMoodleParaDiretorioUnico\\origem'
        destino = 'C:\\Projects\\aulas\\CopiarFicheirosMoodleParaDiretorioUnico\\destino'

copiar_arquivos(origem, destino)