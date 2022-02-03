import sys
if len(sys.argv) < 4:
    print('Введите уровень выработки, размер ставки и сумму премии: ')
else:
    prod = float(sys.argv[1])
    rate = float(sys.argv[2])
    prem = float(sys.argv[3])
    result = prod * rate + prem
    print(f'Размер оплаты труда составляет: {result}')
