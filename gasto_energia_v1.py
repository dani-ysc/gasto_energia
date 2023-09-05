equipamento = input("Qual o nome do equipamento? ")
W = int(input("Quanto de energia (em W) aquele equipamento gasta por hora? "))
horas = int(input("Quantas horas aquele equipamento fica ligado por mês? "))
valor_kwh = float(input("Qual o valor do gasto de energia elétrica por kwh em Petrolina? "))
kwh = (W * horas) / 1000
consumo = kwh * valor_kwh

print("\n") 
print(f"O {equipamento} consome {W}W de energia por hora.")
print(f"Em um cenário em que uma pessoa utiliza aquele aparelho por {horas}h por mês, ")
print(f"na cidade de Petrolina, ela gasta R${consumo:.2f} por mês com aquele equipamento.")
