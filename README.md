# Gasto de energético de um produto

## Sobre

Este projeto contém o progresso de um programa desenvolvido em python para cálculo de energia de um produto em reais (BRL). A ideia por trás dele foi automatizar o cálculo energético de um produto inserindo o gasto do produto em watts, o valor por kw/h daquela cidade e o tempo de consumo diário daquele equipamento. Neste diretório irei reportar todas as fases deste projeto, desde a primeira versão do programa, algumas de suas atualizações, e o detalhamento da versão mais atual do produto.

## Primeira Versão

Eu moro numa cidade bastante quente no nordeste brasileiro. Tinha acabado de comprar um climatizador, e fiquei interessado em saber quanto eu gastaria por mês utilizando aquele equipamento. Vi diversos vídeos do youtube que ensinavam quais as variáveis importantes e como calcular o gasto energético. Aí eu me lembrei que eu sabia programar em python, e decidi criar um script para fornecer o valor do gasto daquele produto.

```
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
```

O programa permite que o usuário realize o input das variáveis importantes para o cálculo. No exemplo do climatizador, em um cenário em que a velocidade está no low e com a função cool ativada, ele consume 150W/h. Na minha cidade, o valor do Kw/h é de 0.706. Eu uso este equipamento cerca de 20h por dia. Levando em consideração um mês com 31 dias, o gasto é de 620h/mês. A primeira versão do programa mostraria a seguinte mensagem levando em consideração as variáveis expostas:

```
O climatizador consome 150W de energia por hora.
Em um cenário em que uma pessoa utiliza aquele equipamento por 620h por mês,
na cidade de Petrolina, ela gasta R$66,66 por mês com aquele equipamento.
```
