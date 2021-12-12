import pandas as pd
path = '/home/maksonvinicio/Documents/GitHub/Data-Science-Projects/Maratona Behind the Code 2021/04_AlgarTech/data/municipios.csv'


def add_city(data):

    data['Cidade'] = 'Cidade'

    data = data[['nome', 'Cidade']]

    data.to_csv('/home/maksonvinicio/Documents/GitHub/Data-Science-Projects/Maratona Behind the Code 2021/04_AlgarTech/data/municipios.csv', index=False, header=False)


data = pd.read_csv(path)
add_city(data)
