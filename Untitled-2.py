preco = float(input("digite o numero: "))
desconto = float(input("digite o numero: "))

valordesconto = preco * desconto/100
precofinal = preco - valordesconto

print("valor do desconto: ", valordesconto)
print("valor final: ", precofinal)