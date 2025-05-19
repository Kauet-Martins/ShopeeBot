import csv
import os

def salvar_csv(nome_arquivo, dados):
    # Caminho da Área de Trabalho do usuário
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Caminho completo do arquivo
    caminho_completo = os.path.join(desktop_path, nome_arquivo)
    
    try:
        with open(caminho_completo, mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["#", "Usuário", "Status"])
            writer.writerows(dados)
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
