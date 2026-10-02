import numpy as np
import pandas as pd

# Aqui pega a primeira aba da planilha ou a aba 0, para pegarmos outras abas
# É necessário especificar isso no código
df_grupo = pd.read_excel('Cotas e Grupos.xlsx')
# É assim que definimos um df(DataFrame), podendo ser vários tipos de arquivos.

#print(df_grupo)
#print("-----------")

# Usando o head podemos definir quantas linhas queremos exibir, sendo número positivo
# a quantidade a exibir, número negativo a quantidade de linhas que não irá exibir
# a partir da última
#print(df_grupo.head(2))

# Dessa maneira escolhemos qual aba queremos pegar
df_cotas = pd.read_excel('Cotas e Grupos.xlsx', sheet_name=1)

#print(df_cotas)
#print("-----------")
#print(df_cotas.head(2))
#print(df_cotas.shape)
# Usamos .shape para termos uma descrição do dataframe, onde se passamos sem índex
# retorna a quantidade de linhas e colunas, se passamos com [0] retorna apenas as 
# linhas e se passamos com [1] somente a quantidade de colunas
# print(df_cotas.columns)
# Usamos .columns para retornar o nome das colunas, podemos criar uma lista usando list
# print(list(df_cotas.columns))
df_cotas2 = df_cotas.copy()
df_cotas2.loc[2:5, 'Cota'] = None
# Podemos usar o isnull para identificar os campos nulos
# print(df_cotas2.isnull().head(7))
# Podemos ainda usar junto com o sum para saber quantos nulos tem em cada coluna
# print(df_cotas2.isnull().sum())
# Ou quantos nulos tem no total
# print(df_cotas2.isnull().sum().sum())

df_cotas_teste = pd.read_excel('Cotas e Grupos.xlsx', sheet_name=2)

# Podemos ainda classificar um datafrase usando uma ou mais colunas como base
# print(df_cotas_teste)
# print("")
# print("-------------")
# print("")
# df_cotas_teste.sort_values(by="assembleia", ascending=True, inplace=True)
# Nessa função, o ascending indica a ordem (crescente ou decrescente) e o inplace
# indica se vai fazer a alteração e retornar um dataframe nome (para isso precisamos
# reatribuir o resultado à variável. Exemplo: df = df.dropna()) em caso de false
# Ou se a função vai alterar o objeto que já existe em caso de false.
# print(df_cotas_teste)

# Para classificar por várias colunas
df_cotas_teste.sort_values(by=["assembleia", "Cota"], ascending=True, inplace=True)
# print(df_cotas_teste)

# Quando realizamos uma classificação ou filtro, o indice pode ficar desorganizado
# Para reorganizar usamos
df_cotas_teste.reset_index(drop=True, inplace=True)
# Nesse código o drop=true joga o índice antigo fora, se fosse false ele criaria
# uma nova coluna
# print(df_cotas_teste)

# Para extrair os dados com base em uma condição usamos
# print(df_cotas_teste[df_cotas_teste["assembleia"] > 66])

# Podemos também isolar uma única coluna usando [], ao fazer isso adquirimos uma
# Série, que é um campo unidimensional que contém qualquer tipo de dado
# Um DataFrame é composto por várias séries, que funcionam como colunas
# print(df_cotas_teste['Cota'])

# Se quisermos podemos isolar mais de uma coluna ou série de uma vez
# print(df_cotas_teste[['Cota', 'assembleia']]) #OBS: aqui precisa de dois [] ([[]])

# Podemos também isolar uma única linha usando um tipo de booleano. Dessa maneira
# Trazemos junto também a coluna de cabeçalho
# print(df_cotas_teste[df_cotas_teste.index==2])
# Ou seja, aonde o index for exatamente igual a 2

# Podemos também isolar duas ou mais linhas usando o método isnin(range()) ao invés de 
# operador booleano
# print(df_cotas_teste[df_cotas_teste.index.isin(range(2,4))])

# Podemos buscar linhas específicas por rótulos ou condições
# Aqui redefinimos o índex para começar no 1 ao invés de 0 como o Pandas faz por padrão
# Serve também para criar o index novo quando ele esta desorganizado por filtro
df_cotas_teste.index = range(1, 22)
# O .loc[] um rótulo para apontar para uma linha, coluna ou série, enquanto iloc[]
# usa a posição numérica 
# Pode ser uma única linha ou um intervalo, usando .loc[n:y]
# print(df_cotas_teste.loc[21])
# print(df_cotas_teste.iloc[1])

# Podemos ainda pegar um subconjunto com .loc e iloc, usando uma lista em vez de 
# um intervalo
# print(df_cotas_teste.loc[[1, 5, 10]])

# Ainda sobre .loc[] e .iloc[], podemos também escolher as colunas específicas
# No caso do .loc[] usamos apenas o nome, no caso de iloc[] temos que usar as
# posições das colunas
# print(df_cotas_teste.loc[1:3, ['Cota', 'assembleia']])
# print(df_cotas_teste.iloc[1:3, :2])
