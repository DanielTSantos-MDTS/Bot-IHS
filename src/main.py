import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Aqui pega a primeira aba da planilha ou a aba 0, para pegarmos outras abas É necessário especificar isso no código
df_grupo = pd.read_excel("../Bot-IHS/data/Cotas e Grupos.xlsx")
# É assim que definimos um df(DataFrame), podendo ser vários tipos de arquivos.

# print(df_grupo) print("-----------")

# Usando o head podemos definir quantas linhas queremos exibir, sendo número positivo a quantidade a exibir, número negativo a quantidade de linhas que não irá exibir a partir da última print(df_grupo.head(2))

# Dessa maneira escolhemos qual aba queremos pegar
df_cotas = pd.read_excel("../Bot-IHS/data/Cotas e Grupos.xlsx", sheet_name=1)

# print(df_cotas) print("-----------")

# print(df_cotas.head(2))

# print(df_cotas.shape) Usamos .shape para termos uma descrição do dataframe, onde se passamos sem índex retorna a quantidade de linhas e colunas, se passamos com [0] retorna apenas as linhas e se passamos com [1] somente a quantidade de colunas print(df_cotas.columns)

# Usamos .columns para retornar o nome das colunas, podemos criar uma lista usando list print(list(df_cotas.columns))
df_cotas2 = df_cotas.copy()
df_cotas2.loc[2:5, "Cota"] = None

# Podemos usar o isnull para identificar os campos nulos print(df_cotas2.isnull().head(7))

# Podemos ainda usar junto com o sum para saber quantos nulos tem em cada coluna print(df_cotas2.isnull().sum())

# Ou quantos nulos tem no total print(df_cotas2.isnull().sum().sum())

df_cotas_teste = pd.read_excel("../Bot-IHS/data/Cotas e Grupos.xlsx", sheet_name=2)

# Podemos ainda classificar um datafrase usando uma ou mais colunas como base print(df_cotas_teste) print("") print("-------------") print("")

# df_cotas_teste.sort_values(by="assembleia", ascending=True, inplace=True) Nessa função, o ascending indica a ordem (crescente ou decrescente) e o inplace indica se vai fazer a alteração e retornar um dataframe nome (para isso precisamos reatribuir o resultado à variável. Exemplo: df = df.dropna()) em caso de false Ou se a função vai alterar o objeto que já existe em caso de false. print(df_cotas_teste)

# Para classificar por várias colunas
df_cotas_teste.sort_values(by=["assembleia", "Cota"], ascending=True, inplace=True)
# print(df_cotas_teste)

# Quando realizamos uma classificação ou filtro, o indice pode ficar desorganizado Para reorganizar usamos
df_cotas_teste.reset_index(drop=True, inplace=True)
# Nesse código o drop=true joga o índice antigo fora, se fosse false ele criaria uma nova coluna print(df_cotas_teste)

# Para extrair os dados com base em uma condição usamos print(df_cotas_teste[df_cotas_teste["assembleia"] > 66])

# Podemos também isolar uma única coluna usando [], ao fazer isso adquirimos uma Série, que é um campo unidimensional que contém qualquer tipo de dado Um DataFrame é composto por várias séries, que funcionam como colunas print(df_cotas_teste['Cota'])

# Se quisermos podemos isolar mais de uma coluna ou série de uma vez print(df_cotas_teste[['Cota', 'assembleia']]) #OBS: aqui precisa de dois [] ([[]])

# Podemos também isolar uma única linha usando um tipo de booleano. Dessa maneira Trazemos junto também a coluna de cabeçalho print(df_cotas_teste[df_cotas_teste.index==2]) Ou seja, aonde o index for exatamente igual a 2

# Podemos também isolar duas ou mais linhas usando o método isnin(range()) ao invés de operador booleano print(df_cotas_teste[df_cotas_teste.index.isin(range(2,4))])

# Podemos buscar linhas específicas por rótulos ou condições Aqui redefinimos o índex para começar no 1 ao invés de 0 como o Pandas faz por padrão Serve também para criar o index novo quando ele esta desorganizado por filtro
df_cotas_teste.index = range(1, 22)

# O .loc[] um rótulo para apontar para uma linha, coluna ou série, enquanto iloc[] usa a posição numérica Pode ser uma única linha ou um intervalo, usando .loc[n:y] print(df_cotas_teste.loc[21]) print(df_cotas_teste.iloc[1])

# Podemos ainda pegar um subconjunto com .loc e iloc, usando uma lista em vez de um intervalo print(df_cotas_teste.loc[[1, 5, 10]])

# Ainda sobre .loc[] e .iloc[], podemos também escolher as colunas específicas No caso do .loc[] usamos apenas o nome, no caso de iloc[] temos que usar as posições das colunas print(df_cotas_teste.loc[1:3, ['Cota', 'assembleia']]) print(df_cotas_teste.iloc[1:3, :2])

# Podemos atualizar ou modificar os valores usando a atribuição "=" df_cotas_teste.loc[df_cotas_teste['assembleia'] == 7, ['assembleia']] = 2 Nesse código usamos o == para localizar a linha que tenha esse valor, ou seja Como se fosse um filtro. Já o ", ['assembleia']", serve para especificar que dentro das linhas encontradas, a única coluna que vai ser alterada é 'assembleia'. print(df_cotas_teste.loc[df_cotas_teste['assembleia'] == 2])

# Podemos ainda usar um filtro de condicional para localizar uma linha print(df_cotas_teste[df_cotas_teste.Cota == 694])

# Podemos também usar comparações com >< no loc e especificar quais colunas buscar print(df_cotas_teste.loc[df_cotas_teste['assembleia'] > 60, ['Cota', 'R', 'D']]) Aqui, no .loc[df['assembleia'] > 60] é onde fazemos o filtro e após a vírgula é onde colocamos as colunas que queremos

# =========================================================
# ================== Tratamento de dados ==================
# =========================================================

# ================= Eliminação dos dados ==================

# Temos algumas tratativas para dados nulos, uma das mais comuns é a eliminação desses dados em situações em que se há muitos dados e a perda de alguns dados não afetará a análise. Para isso, podemos usar o método .dropna(). O .dropna() remove a linha que contenha valor nulo. Podemos definir se queremos apagar a linha ou a coluna usando o parâmetro axis= que por padrão é 0 e remove as linhas, se colocarmos 1 ele apaga a coluna com esses valores
# df_cotas_teste = df_cotas_teste.dropna(axis=1)
# Além do axis, temos também o parâmetro how=, que define o critério de remoção, sendo any se qualquer um for nulo, ou all que apaga somente se todos forem nulos. Temos também o subset, que lista as colunas específicas para serem analisadas para remoção e o inplace= que como já vimos, que define se vai alterar o dataframe original, ou criar um novo com as alterações. Se usamos o false, precisamos fazer um salvamento de dados em um novo dataframe
# df_cotas_teste.dropna(inplace=False)
# print(df_cotas_teste.shape)

# ================= Substituição dos valores ==================

# Em vez de eliminar, podemos substituir os valores ausentes por uma estatística resumida ou um valor específico. Podemos substituir o valor ausente pela média de linhas ou colunas

valor_medio = df_cotas_teste["assembleia"].mean()
df_cotas_teste = df_cotas_teste.fillna(valor_medio)

# print(df_cotas_teste.head())

# ================= Lidando com Dados Duplicados ==================
df_cotas_teste_duplicata = df_cotas_teste.copy()
df_cotas_teste_duplicata = pd.concat([df_cotas_teste, df_cotas_teste_duplicata])
# Podemos eliminar todas as linhas duplicadas usando o método .drop_duplicates()
# df_cotas_teste_duplicata = df_cotas_teste_duplicata.drop_duplicates()
# Podemos eliminar as duplicatas com base em uma coluna específica usando subset=['']
# df_cotas_teste_duplicata = df_cotas_teste.drop_duplicates(subset=['assembleia'])
# Temos o keep para definir o comportamento da remoção, tendo first, last ou false (padrão), que apaga todas as linhas e tem também o inplace=
# print(df_cotas_teste_duplicata.shape)

# ================= Renomeando Colunas ==================

# É muito comum termos a necessidade de renomear colunas, para fazermos isso, utilizamos o método .rename(columns = {'Nome coluna' : 'Nome novo'}, inplace = true)
# df_cotas_teste.rename(columns= {'Cota' : 'cota'}, inplace = True)
# print(df_cotas_teste.head())

# Podemos ainda passar uma lista para renomear diretamente na ordem que aparece
# df_cotas_teste.columns = ['cota', 'r', 'd', 'Assembleia', 'Grupo']
# print(df_cotas_teste.head())

# ================= Operadores Matemáticos ==================

# Para tratativas matemáticas, temos alguns operadores. Como o mean() (usando anteriormente) para média, para calcular a moda temos .mode() e para calcular mediana temos .median().

# ================= Criação de Novas Colunas ==================

# Podemos criar novas colunas com base em colunas já existente
df_cotas_teste["assembleia"] = df_cotas_teste["assembleia"].astype("Int64")
df_cotas_teste["assembleia"] = pd.NA
df_cotas_teste.dropna(axis=1, inplace=True)
df_cotas_teste["teste"] = df_cotas_teste["Cota"] / 2 + df_cotas_teste["D"]
# print(df_cotas_teste.head())

# ================= Contagens de Valores ==================

# Podemos contar a quantidade de valores distintos, por exemplo, vamos contar a quantidade de valores repetidos na coluna R
# print(df_cotas_teste['R'].value_counts())

# Podemos ainda ver a proporção de cada um com o parâmetro normalize=
# print(df_cotas_teste['R'].value_counts(normalize=True))

# Podemos ainda escolher se a ordenação vai ser automática ou não, por padrão é ativada (sort=True), mas podemos colocar sort=False.
# print(df_cotas_teste['R'].value_counts(sort=False))

# Podemos ainda contar mais de uma coluna na contagem usando o subset=
# print(df_cotas_teste.value_counts(subset=['R', 'D']))

# ================= Agrupamento de Valores ==================

# O pandas permite agregação de valores a partir do agrupamento de valores de colunas específicas. Para fazer isso, usamos o .groupby() juntamente com um método de resumo (.mean(), .sum(), .agg(), .median())
# print(df_cotas_teste.groupby('R').mean())

# O groupby() permite ainda agrupar por mais de uma coluna, passando uma lista de nomes []
# print(df_cotas_teste.groupby(["R", "D"]).mean())

# ================= Criação de Tabela Dinâmica ==================

# O pandas permite também a criação de tabelas dinâmicas para facilitar a obtenção de valores com base em combinação de variáveis
df_dinamic = pd.pivot_table(
    df_cotas2,
    values="Cota",
    index="assembleia",
    columns=["R"],
    aggfunc="count",
    fill_value=0,
)
# Nesse código o values é o que define qual coluna vai ser analisada.
# Os valores da tabela final será calculada a partir dessa coluna.
# Index, define por qual coluna será definida a organização das linhas da tabela.
# Columns define que as colunas da nova tabela serão divididas pelos valores da coluna especificada.
# aggfunc Define a função de agregação, neste caso vai ser uma contagem, mas pode ser algum método de resumo do numpy como mean() usando np.mean()
# fill_value serve para preencher automaticamente qualquer valor nulo (NaN) que tenha na tabela final da tabela dinâmica por um valor escolhido
# print(df_dinamic)

# ================= Criação de Tabela Dinâmica ==================

# O pandas permite que trace as relações entre as variáveis usando gráficos de linha

# df_cotas2[["Valor Parcela", "Prazo"]].plot.line("Prazo", "Valor Parcela")
# Aqui criamos um gráfico de linhas, ao usar o plot.line(), o eixo X (horizontal), será preenchido automaticamente pelo índice do dataframe e o eixo y mostrará os valores numéricos

# ================= Criação de Gráficos ==================

# O pandas nos permite criar gráficos em conjunto com o matplotlib

# ================= Gráfico de Linhas ==================

# Para usar esse comando precisamos ter o matplotlib instalado no venv e importado no arquivo
# plt.savefig('Grafico1.png')
# Esse comando guarda o gráfico em um ficheiro de imagem na pasta raiz do projeto.
# df_cotas2[["Valor Parcela", "Prazo"]].plot.line(
#     figsize=(20, 10), color={"Valor Parcela": "Red", "Prazo": "blue"}
# )

# Podemos também, usar todas as tabelas do conjunto no gráfico
# df_cotas2.plot.line(subplots=True)


# ================= Gráfico de Barras ==================

# Para criação de gráficos de barras, podemos usar a contagem de categorias para visualizar a distribuição

# df_cotas2['Prazo'].value_counts().plot.bar()

# ================= Gráfico de Caixas ==================

# O pandas permite ainda a distribuição de quartis de variáveis contínuas para visualizar em um boxplot()

# df_cotas2.boxplot(column = 'Cota', by='Prazo')

# plt.savefig("Grafico3.png")

# ================= Iteração Linha a Linha ==================

# No pandas, temos também a funcionalidade de iteração a cada linha, ou seja, leitura de linha a linha. Para isso, usamos o iterrows()

row = next(df_cotas2.iterrows())[1]
# O next serve para obter o próximo item do iterador imediatamente, similar a um loop for com um break na primeira execução
# E o número [1] serve para descartar o índice

# ================= Verificação de Valores Ausentes ==================

# No pandas, temos o método .isna(), que serve para detectar e identificar valores ausentes ou nulos (NaN, None, NaT) em uma série ou dataframe, ele vai retornar uma estrutura com o mesmo tamanho, com True onde o valor é nulo ou ausente e false onde ha um valor preenchido

# print(df_cotas2.isna())
# Podemos usar com o sum() para ver a quantidade por coluna e o .sum().sum() para ver a quantidade por dataframe
# print(df_cotas2.isna().sum())

# print(df_cotas2.isna().sum().sum())

# OBS: Existe também um método contrário, para saber onde NÃO é nulo, que é o .notna()

# ========= Tarefa 1 ===============

# for linha in df_cotas2.iterrows():
# OBS: em python, o iterrows() devolve uma tupla, ou seja em formato de (indíce, dados) agrupados e tuplas só aceitam valores por índice. Para conseguir fazer esse tipo de comparação booleana, precisamos desagrupar o índice e os dados da tupla.
for indice, linha in df_cotas.iterrows():
    if pd.notna(linha["Grupo"]):
        # print("A cota ", linha["Cota"], "Possui Grupo")
        # Podemos usar strings formatadas para facilitar
        print(f"A cota {linha['Cota']}, já possui Grupo")
    else:
        assembleia_base = linha["assembleia"]
# ========= Tarefa 2 ===============
        assembleia_minima = assembleia_base - 2
        assembleia_maxima = assembleia_base + 2
        print(
            f"A cota {linha['Cota']}, não possui Grupo. A assembleia base é: {linha['assembleia']}. Buscando grupos entre {assembleia_minima} e {assembleia_maxima}"
        )
        grupos = df_grupo['assembleia'].between(assembleia_minima, assembleia_maxima)
        grupos_correspondente = df_grupo[grupos]["grupo"] # Aqui faz o filtro e pega apenas a coluna grupo com base no filtro
        print(f"Grupos que batem com a assembleia: {grupos_correspondente.tolist()}")
        # Aqui usamos tolist() para retornar uma lista lado a lado e retirar o índice
        break

