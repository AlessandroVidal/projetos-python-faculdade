print("Desenvolvido por Alessandro Vidal Bispo | RU - 5478620")
print("Bem-vindo ao sistema de camisetas - PH.STORE CAMISETAS")


def escolha_modelo():
    while True:
        modelo = input("Escolha o modelo (MCS, MLS, MCE, MLE): ").upper()

        if modelo == "MCS":
            return 22.0
        elif modelo == "MLS":
            return 29.0
        elif modelo == "MCE":
            return 40.0
        elif modelo == "MLE":
            return 55.0
        else:
            print("Modelo inválido. Tente novamente.")


def num_camisetas():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de camisetas (máx. 3000): "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que 0.")
                continue

            if quantidade > 3000:
                print("Quantidade não permitida. Máximo: 3000.")
                continue

            # Desconto por quantidade (exemplo comum):
            # >= 2000: 35%
            # >= 1500: 25%
            # >= 150:  19%
            # senão:   0%
            if quantidade >= 2000:
                desconto = 0.35
            elif quantidade >= 1500:
                desconto = 0.25
            elif quantidade >= 150:
                desconto = 0.19
            else:
                desconto = 0.0

            return quantidade, desconto

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def frete():
    while True:
        tipo = input("Digite o tipo de frete (0-retirada | 1-transportadora | 2-correios): ")

        if tipo == "0":
            return 0.0
        elif tipo == "1":
            return 200.0
        elif tipo == "2":
            return 400.0
        else:
            print("Frete inválido. Digite 0, 1 ou 2.")


preco_unitario = escolha_modelo()
quantidade, desconto = num_camisetas()
valor_frete = frete()

subtotal = preco_unitario * quantidade
subtotal_com_desconto = subtotal * (1 - desconto)
total = subtotal_com_desconto + valor_frete

print("\n----- Seu pedido -----")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Desconto: {desconto*100:.0f}%")
print(f"Subtotal (com desconto): R$ {subtotal_com_desconto:.2f}")
print(f"Frete: R$ {valor_frete:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
