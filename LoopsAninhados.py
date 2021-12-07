dados = [
['Rodas de liga', 'travas', 'piloto automatico', 'bancos de couro', 'ar cond', 'sensor de estacionamento', 'sensor crepuscular'],
['central multimidia', 'teto panoramico', 'freio abs', '4 x 4', 'painel digital', 'bancos de couro'],
['Piloto automatico', 'controe de estab', 'sensor crepuscular', 'bancos de couro']
]

print(dados)

for lista in dados:
    for item in lista:
        print(item)


Acessorios1 = []

for lista in dados:
    for item in lista:
        Acessorios1.append(item)

#comando set remove duplicatas de sequencias

list(set(Acessorios1))
print(Acessorios1)    



