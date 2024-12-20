# Elabore um programa que calcule o valor a ser pago por um produto.
# Considerando o seu preço normal e condição de pagamento:
# Á vista dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartâo: preço normal
# 3X ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[0m')
print('Sua compra de R${:.2f} vai custar R${} no final.'.format(preço, total))