#Calculador de fatura
#Por: Gleyson

print ("Calcule sua fatura mediante os minutos utilizados!")
minutos = float(input("Quantos minutos você utilizou?:\n")) # entra com valor flutuante na variavel minutos
if minutos <= 199:
    fatura = (minutos * 0.20)
    print("Não houve descontos")
elif minutos <= 400 and minutos >= 200:
    fatura = (minutos * 0.18)
    print("Desconto de 0.02 centavos por minuto")
elif minutos >= 401 and minutos <= 800:
    fatura = (minutos * 0.15)
    print("Desconto de 0.05 centavos por minuto")
else:
    minutos <= 801
    fatura = (minutos * 0.08)
    print("Desconto de 0.12 centavos por minuto")
print("Sua fatura é de: R$%1.2f" %fatura)

#teste


