nota1 = float(input("digite a nota do primeir bimestre: "))
nota2 = float(input ("digite a nota do segundo bimestre:"))
nota3 = float(input ("digite a nota do terceiro bimestre:"))
nota4 = float(input("digite a nota do quarto bimestre:"))

media = (nota1 + nota2 + nota3 + nota4)/4

if media <=5:
    print("recuperação")
elif media <=3:
    print("recuperação")
else:
    print("aprovado")

    