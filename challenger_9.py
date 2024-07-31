# 2 - Utilizando o dicionário criado no item 1:
# - Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# - Adicione um campo de profissão para essa pessoa;
# - Remova um item do dicionário.

pessoa = [{'nome':'Richard' ,'idade':'24','cidade':'Rio de Janeiro'}]

for items in pessoa:
    nome_pessoa = items['nome']
    idade_pessoa = items['idade']
    cidade_pessoa = items['cidade']
    
print(f' Nome: {nome_pessoa} \n Idade: {idade_pessoa} \n Cidade: {cidade_pessoa}')