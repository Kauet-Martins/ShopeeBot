import tkinter as tk
from tkinter import messagebox
import threading
from automacao import navegador, seguidores, seguindo

estado = {"driver": None}

def iniciar_navegador():
    def run():
        estado["driver"] = navegador.abrir_navegador()
        messagebox.showinfo("Login", "Faça login manualmente e depois clique em OK.")
        navegador.salvar_cookies(estado["driver"])
        atualizar_status("✅ Login salvo com sucesso!")
    threading.Thread(target=run).start()

def seguir():
    def run():
        shop_id = id_entry.get().strip()
        try:
            quantidade = int(quantidade_entry.get().strip())
        except ValueError:
            atualizar_status("❌ Quantidade inválida.")
            return

        if not estado["driver"] or not shop_id:
            atualizar_status("❌ Navegador não iniciado ou ID inválido.")
            return
        seguidores.seguir_usuarios(estado["driver"], shop_id, atualizar_status, quantidade)
    threading.Thread(target=run).start()

def deixar_de_seguir():
    def run():
        shop_id = id_entry.get().strip()
        try:
            quantidade = int(quantidade_entry.get().strip())
        except ValueError:
            atualizar_status("❌ Quantidade inválida.")
            return

        if not estado["driver"] or not shop_id:
            atualizar_status("❌ Navegador não iniciado ou ID inválido.")
            return
        seguindo.deixar_de_seguir(estado["driver"], shop_id, atualizar_status, quantidade)
    threading.Thread(target=run).start()

def atualizar_status(msg):
    status_label.config(text=msg)

# Interface Tkinter
root = tk.Tk()
root.title("Shopee Automação")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="🔧 ID da Loja:", font=("Arial", 12)).pack(pady=(20, 5))
id_entry = tk.Entry(root, font=("Arial", 12), justify="center")
id_entry.pack()

tk.Label(root, text="👥 Quantidade para seguir/deixar de seguir:", font=("Arial", 12)).pack(pady=(10, 5))
quantidade_entry = tk.Entry(root, font=("Arial", 12), justify="center")
quantidade_entry.insert(0, "20")  # valor padrão
quantidade_entry.pack()

tk.Button(root, text="🔓 Login manual", font=("Arial", 11), command=iniciar_navegador).pack(pady=10)
tk.Button(root, text="📥 Seguir seguidores", font=("Arial", 11), command=seguir).pack(pady=5)
tk.Button(root, text="📤 Deixar de seguir", font=("Arial", 11), command=deixar_de_seguir).pack(pady=5)

status_label = tk.Label(root, text="🔹 Aguardando ação...", font=("Arial", 10), fg="blue")
status_label.pack(pady=20)

root.mainloop()
