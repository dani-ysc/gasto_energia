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

## Segunda Versão

A primeira versão possui alguns problemas. Ele pede que o usuário coloque a quantidade de horas mensais que ele usa aquele aparelho, o que faria com que o usuário precisasse realizar o cálculo. Outro problema era relacionado a quantidade de equipamentos que o usuário gostaria de calcular o gasto energético. Da forma como o primeiro programa foi criado, caso ele desejasse verificar o cálculo energético de outro equipamento, ele teria que abrir novamente o programa. Então implementei algumas melhorias no código-fonte para atender essas lacunas encontradas na primeira versão.

```
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
```

A nova versão do programa permite que o usuário coloque a quantidade de horas por dia que utiliza aquele equipamento, e o programa calcula a quantidade de horas totais por mês (considerando um mês com 31 dias, a quantidade máxima de dias possíveis num mês); permite o cálculo de quantos aparelhos o usuário desejar; permite que ele estabeleça uma meta (em reais) que ele gostaria gastar com todos esses equipamentos; e apresenta uma mensagem final congratulando-o caso o gasto tenha sido abaixo do ideal, ou lamentando caso o gasto tenha sido acima da meta estabelecida pelo mesmo.

Em uma cenário que o usuário deseje verificar o gasto de dois equipamentos: um PlayStation 4 que consome 130W/h utilizando-o por 4h diárias, e um climatizador que consome 150W/h utilizando-o por 12h diárias, estabelecendo R$60 como a meta de gasto com esses dois equipamentos, e levando em consideração que o valor por Kwh na minha cidade é de R$0.706, o programa exibiria a seguinte mensagem final:

```
O valor, em reais, pago em energia por mês com esses 2 objetos é de: R$50.78
Muito bem! Seu consumo ficou R$9.22 abaixo do que você gostaria 👏
```
