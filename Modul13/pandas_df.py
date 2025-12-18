import pandas as pd

data={
    'Name':['Daris','Ahmeti','Eris'],
    'Age':[15,25,33],
    'City':['Prishtina','Mitrovic','Gjilan']
}

df=pd.DataFrame(data)
print(df)