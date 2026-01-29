print("Desenvolvido por Alessandro Vidal Bispo | RU - 5478620")

print('--- Bem-vindo ao restaurante Jaime ---')

print('----------------- CARDÁPIO ------------------')
print('---------------------------------------------')
print('---| Tamanho | Bife Acebolado (BA)  | Filé de Frango (FF) | ----')
print('---|    P    |         R$ 16.99     |        R$ 11.99     | ----')
print('---|    M    |         R$ 20.30     |        R$ 13.99     | ----')
print('---|    G    |         R$ 32.50     |        R$ 19.99     | ----')
print('---------------------------------------------')

print('Pratos à disposição:')
print('BA - Bife Acebolado')
print('FF - Filé de Frango')
print('Tamanhos disponíveis: P (Pequeno), M (Médio), G (Grande)')

total_pedido = 0.0

while True:
    sabor = input('Digite o sabor desejado (BA/FF): ').upper()
    if sabor not in ('BA', 'FF'):
        print('Sabor inválido. Tente novamente.')
        continue

    tamanho = input('Digite o tamanho desejado (P/M/G): ').upper()
    if tamanho not in ('P', 'M', 'G'):
        print('Tamanho inválido. Tente novamente.')
        continue

    # Define preço
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16.99
        elif tamanho == 'M':
            preco = 20.30
        else:  # G
            preco = 32.50
    else:  # FF
        if tamanho == 'P':
            preco = 11.99
        elif tamanho == 'M':
            preco = 13.99
        else:  # G
            preco = 19.99

    total_pedido += preco
    print('Item adicionado! Valor: R$ {:.2f}'.format(preco))

    continuar = input('Deseja pedir algo a mais? [S/N]: ').upper()
    if continuar == 'N':
        break

print('Total do pedido: R$ {:.2f}'.format(total_pedido))
