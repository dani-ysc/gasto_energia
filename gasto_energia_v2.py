n = int(input("Quantos equipamentos você irá verificar o gasto energético? "))
gasto_ideal = float(input("Quantos reais você gostaria gastar com esses equipamentos? R$"))
cidade = input("Qual o nome da cidade que você reside? ")

gasto_total = 0
for i in range(0, n):
    equipamento = input("Qual o nome do equipamento? ")
    W = int(input("Quanto de energia (em W) aquele equipamento gasta por hora? "))
    horas_dia = int(input("Quantas horas aquele equipamento fica ligado por dia? "))
    horas = horas_dia * 31
    valor_kwh = float(input("Qual o valor do gasto de energia elétrica por kwh em Petrolina? "))
    kwh = (W * horas) / 1000
    consumo = kwh * valor_kwh
    gasto_total += consumo

    print("\n") 
    print(f"O {equipamento} consome {W}W de energia por hora.")
    print(f"Em um cenário em que uma pessoa utiliza aquele aparelho por {horas_dia}h por dia, ")
    print(f"na cidade de {cidade}, ela gasta R${consumo:.2f} por mês com aquele equipamento.")

consumo_restante = gasto_ideal - gasto_total

print("\n") 
print(f"O valor, em reais, pago em energia por mês com esses {n} objetos é de: R${gasto_total:.2f}")

if gasto_total < gasto_ideal:
    print(f"Muito bem! Seu consumo ficou R${consumo_restante:.2f} abaixo do que você gostaria 👏")
elif gasto_total > gasto_ideal:
    print(f"Seu consumo foi de R${-consumo_restante:.2f} acima do desejado 😔")
