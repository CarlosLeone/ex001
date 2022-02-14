d = int(input('Quantos dias rodados? '))
k = float(input('Quantos KM rodados?'))
p = (60 * d) + (0.15 * k)
print('O valor a ser pago é R${:.2f} '.format(p))
