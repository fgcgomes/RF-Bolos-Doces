def ler_vendas():
    try:
        # Abrir o arquivo vendas.txt para leitura
        with open("vendas.txt", mode="r") as file:
            vendas = file.readlines()

        if not vendas:
            print("Não há vendas registradas.")
            return

        # Exibir os dados das vendas
        print(f"{'Data da Venda':<20} {'Cliente':<30} {'Produto':<20} {'Quantidade':<10} {'Valor Total (R$)':<15}")
        print("=" * 95)

        total_geral = 0
        for venda in vendas:
            dados = venda.strip().split(";")

            # Extrair os dados individuais
            data_venda = dados[0].strip()
            nome_cliente = dados[1].strip()
            nome_doce = dados[2].strip()
            quantidade = int(dados[3].strip())
            valor_total = float(dados[5].strip().replace("R$ ", "").replace(",", "."))

            # Exibir cada venda
            print(f"{data_venda:<20} {nome_cliente:<30} {nome_doce:<20} {quantidade:<10} R$ {valor_total:>13.2f}")

            # Somar o total geral
            total_geral += valor_total

        # Exibir o total geral de todas as vendas
        print("=" * 95)
        print(f"{'Total Geral:':<80} R$ {total_geral:.2f}")

    except FileNotFoundError:
        print("O arquivo 'vendas.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo de vendas: {e}")

# Chama a função para exibir as vendas registradas
ler_vendas()
