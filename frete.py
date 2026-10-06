valor = float(input("qual o valor: "))

if valor>=200:
    frete = 0
    total = valor+frete
elif valor>=100:
    frete = 10
    total = valor+frete
else:
    frete = 20 
    total = valor+frete

print("valor total com frete:",total)
