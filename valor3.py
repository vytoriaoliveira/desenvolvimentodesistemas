valor = float(input("digite o valor: "))

if valor >=500:
    print ("desconto de 20%")
    desconto = valor * 0.20
    valorcomdesconto = valor - desconto
    print("valor com desconto",valorcomdesconto) 
elif valor >=200:
    print("desconto de 10%")
    desconto = valor * 0.10
    valorcomdesconto = valor - desconto
    print("valor com desconto",valorcomdesconto)
else:
    print("sem desconto:")
    


