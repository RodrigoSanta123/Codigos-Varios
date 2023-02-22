import sys
coinsOptions = [1,5]
target=20
table = [[0 for x in range(len(coinsOptions)+1)] for x in range(target+1)]
for x in range(len(coinsOptions)+1):
    table[0][x]=1
for col in range(target+1):
    for row in range(1,len(coinsOptions)+1):
        try:
            table[col][row]=table[col][row-1]+table[col-coinsOptions[row-1]][row]
        except:
            print('No es posible pagar este valor con estas monedas')
            sys.exit()
print(table[target][len(coinsOptions)])