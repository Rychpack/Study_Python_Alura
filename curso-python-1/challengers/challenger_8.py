# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = [{'nome':'Richard' ,'idade':'24','cidade':'Rio de Janeiro'}]

for items in pessoa:
    nome_pessoa = items['nome']
    idade_pessoa = items['idade']
    cidade_pessoa = items['cidade']
    
print(f' Nome: {nome_pessoa} \n Idade: {idade_pessoa} \n Cidade: {cidade_pessoa}')