import plotly_express as px
import pandas as pd

dados = pd.read_excel("vendas.xlsx")

#print(dados)
#print(dados.head()) #mostra as primeiras linhas dos dados
#print(dados.tail()) #mostra as ultimas linhas dos dados

#print(dados.shape) #ver a quantidade de linhas e colunas
#print(dados.info()) #mostra os tipos de dados (especificações)
#print(dados["loja"]) #mostra apenas a coluna especificada

#print(dados["preco"].describe().to_frame()) #estatisticas especificadas
#print(dados["loja"].unique()) #lista especifica

#print(dados["loja"].value_counts()) #loja e numero de vendas de cada uma
#print(dados["cidade"].value_counts()) #cidade e numero de vendas de cada cidade

#print(dados["forma_pagamento"].value_counts()) #total de cada forma de pgto

#print(dados.groupby("loja")["preco"].sum()) #agrupado por loja e preco somando 
#print(dados.groupby(["loja", "cidade","forma_pagamento"])["preco"].sum().to_excel("faturamento.xlsx")) #para excel
#print(dados.groupby(["loja", "cidade","forma_pagamento"])["preco"].sum()) #mostra loja, cidade e as formas de pgto junto do total


colunas = ["loja", "cidade", "estado", "regiao", "local_consumo"] 
for coluna in colunas:
    grafico = px.histogram(dados,
             x=coluna, 
             y="preco",
             text_auto=True, 
             title=f"Faturamento por {coluna}",
             color="forma_pagamento")
    grafico.show()
    #grafico.write_html(f"grafico-{coluna}.html")


