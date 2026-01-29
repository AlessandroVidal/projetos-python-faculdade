print("Desenvolvido por Alessandro Vidal Bispo | RU - 5478620")
print("Bem-vindo à loja de fragrâncias")

valor_pedido = float(input("Digite o valor do pedido: R$ "))
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))

if quantidade_parcelas < 4:
    juros = 0
elif quantidade_parcelas < 6:
    juros = 0.04
elif quantidade_parcelas < 9:
    juros = 0.08
elif quantidade_parcelas < 13:
    juros = 0.16
else:
    juros = 0.32

valor_total = valor_pedido * (1 + juros)
valor_parcela = valor_total / quantidade_parcelas

print(f"\nValor do pedido: R$ {valor_pedido:.2f}")
print(f"Quantidade de parcelas: {quantidade_parcelas}")
print(f"Taxa de juros: {juros * 100:.0f}%")
print(f"Valor total com juros: R$ {valor_total:.2f}")
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
