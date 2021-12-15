import pandas as pd
import matplotlib.pyplot as plt

titanic_prova = pd.read_csv('titanic_prova.csv')
print(titanic_prova.head(10))#Imprime os 10 primeiros valores

titanic_prova.sort_values(by = ['Name'], ascending=True, inplace=True)#Ordena a base de dados por nome
print(titanic_prova.head)#Imprime todos os valores em ordem alfabetica

titanic_prova['Sobrevivente'] = titanic_prova['Survived'].map({0:'Nao', 1:'Sim'})#Cria a serie Sobrevivente

titanic_prova = titanic_prova.drop(columns = ['SibSp', 'Parch' ,'Ticket'])#Remocao dessas colunas
print(titanic_prova.head)#Imprime os valores sem essa colunas

#Colunas que faltavam sendo renomeadas
titanic_prova = titanic_prova.rename({"PassengerId":"Passageiro ID"},axis = "columns")
titanic_prova = titanic_prova.rename({"Pclass":"Classe P"},axis = "columns")
titanic_prova = titanic_prova.rename({"Name":"Nome"},axis = "columns")
titanic_prova = titanic_prova.rename({"Sex":"Sexo"},axis = "columns")
titanic_prova = titanic_prova.rename({"Age":"Idade"},axis = "columns")
titanic_prova = titanic_prova.rename({"Fare":"Tarifa"},axis = "columns")
titanic_prova = titanic_prova.rename({"Cabin":"Cabine"},axis = "columns")
titanic_prova = titanic_prova.rename({"Embarked":"Embarcou"},axis = "columns")

titanic_prova['Sexo'] = titanic_prova['Sexo'].replace(['male','female'],['masculino','FEMININO'])#Alterando os valores de male e famele

classsobrevivente = titanic_prova.groupby(['Classe P','Sobrevivente'])['Sobrevivente'].count()#Numero de sobreviventes por classe
print(classsobrevivente.head)#Imprime o numero de sobreviventes

mortosporsexo = titanic_prova.groupby (["Sexo","Sobrevivente"])["Sexo"].count()#Numero de mortos por sexo
print (mortosporsexo)#Imprime o numero de mortos

classsobrevivente.plot(kind="pie")#Cria um grafico
plt.show()

titanic_prova.to_excel("Pedro Henrique ProvaOPI.xlsx", index=False, header=True)#Exporta o dataframe pra xlsx