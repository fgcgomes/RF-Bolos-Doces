import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

# Função para ler e exibir as vendas
def ler_vendas():
    try:
        # Abrir o arquivo vendas.txt para leitura
        with open("vendas.txt", mode="r") as file:
            vendas = file.readlines()

        if not vendas:
            messagebox.showinfo("Sem Vendas", "Não há vendas registradas.")
            return

        # Limpar a TreeView para novas vendas
        for item in treeview.get_children():
            treeview.delete(item)

        total_geral = 0
        for venda in vendas:
            dados = venda.strip().split(";")

            # Extrair os dados individuais
            data_venda = dados[0].strip()
            nome_cliente = dados[1].strip()
            nome_doce = dados[2].strip()
            quantidade = int(dados[3].strip())
            valor_total = float(dados[5].strip().replace("R$ ", "").replace(",", "."))

            # Adicionar dados na tabela (Treeview)
            treeview.insert("", "end", values=(data_venda, nome_cliente, nome_doce, quantidade, f"R$ {valor_total:.2f}"))

            # Somar o total geral
            total_geral += valor_total

        # Exibir o total geral na label
        label_total.config(text=f"Total Geral: R$ {total_geral:.2f}")

    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo 'vendas.txt' não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo de vendas: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Relatório de Vendas - RF Bolos & Doces")

# Definir o tamanho da janela
root.geometry("800x600")

# Alterar a cor de fundo da janela principal
root.configure(bg="#D3B0FF")  # Cor lavanda suave

# Criar título
title_label = tk.Label(root, text="Relatório de Vendas", font=("Arial", 10, "bold"), bg="#D3B0FF", fg="darkblue")
title_label.pack(pady=20)

# Criar Treeview para mostrar as vendas
columns = ("Data da Venda", "Cliente", "Produto", "Quantidade", "Valor Total (R$)")
treeview = ttk.Treeview(root, columns=columns, show="headings", height=15)

# Estilizando a Treeview
treeview.heading("Data da Venda", text="Data da Venda", anchor="center")
treeview.heading("Cliente", text="Cliente", anchor="center")
treeview.heading("Produto", text="Produto", anchor="center")
treeview.heading("Quantidade", text="Quantidade", anchor="center")
treeview.heading("Valor Total (R$)", text="Valor Total (R$)", anchor="center")

# Definir largura e centralizar as colunas
for col in columns:
    treeview.column(col, anchor="center", width=150)

treeview.pack(pady=20)

# Label para mostrar o total geral
label_total = tk.Label(root, text="Total Geral: R$ 0.00", font=("Arial", 10, "bold"), bg="#D3B0FF", fg="darkblue")
label_total.pack(pady=10)

# Botão para ler as vendas
button_ler_vendas = tk.Button(root, text="Carregar Vendas", font=("Arial", 10, "bold"), command=ler_vendas, bg="#4CAF50", fg="white")
button_ler_vendas.pack(pady=10)

# Iniciar o aplicativo
root.mainloop()
