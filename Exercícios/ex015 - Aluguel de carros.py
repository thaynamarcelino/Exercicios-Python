dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos km rodados? '))
pago = (60 * dias) + (Km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))