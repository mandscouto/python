import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

type (df)

df.head() #Exibe as 5 primeiras linhas

df.tail() #Exibe as 5 últimas linhas

df.shape #Exibe a quantidade de linhas e colunas

df.columns #Exibe um array com o nome das colunas

df.duplicated().sum() #Verifica linhas duplicadas