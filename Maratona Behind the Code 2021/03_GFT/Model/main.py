import pandas as pd
import numpy as np


def unpack_services(answers) -> pd.DataFrame:
    """[unpack the services column]

    Args:
        answers ([dataframe]): [Dataframe with the answers of the user]

    Returns:
        pd.DataFrame: [Dataframe with the answers and with the services column]
    """
    aux = []
    services = []
    for val in range(answers.shape[0]):
        for cols in answers.columns[5::]:
            if answers[cols][val] == 'T':
                aux.append(cols)
            else:
                continue
        services.append(aux)
        aux = []
    answers['services'] = services

    return answers


def unpack_consequents(answers, rules) -> pd.DataFrame:
    """[summary]

    Args:
        answers ([type]): [description]
        rules ([type]): [description]

    Returns:
        pd.DataFrame: [description]
    """
    consequents = []
    i = 0
    for j in range(answers.shape[0]):
        if set(rules['antecedents'][i]) & set(answers['services'][j]):
            consequents.append(rules['consequents'][i])
        else:
            consequents.append(None)
        if i == rules.shape[0] - 1:
            i = 0
        i += 1
    return consequents


def recommendation(answers, rules) -> pd.DataFrame:
    """[Function to recommend a service]

    Args:
        answers ([dataframe]): [Dataframe with the answers of the user]
        rules ([type]): [Dataframe with the rules of the association rules]
    """

    # Verifica todas as marcacoes de answer e retorna uma lista de lista com todas as marcacoes

    answers = unpack_services(answers)

    # Preenche o dataframe com as marcacoes dos consequentes
    consequents1 = []
    consequents2 = []
    consequents3 = []
    confidence1 = []
    confidence2 = []
    confidence3 = []
    i = 0
    for j in range(answers.shape[0]):
        if set(rules['antecedents'][i]) & set(answers['services'][j]):
            try:
                consequents1.append(list(rules['consequents'][i])[0])
                confidence1.append(rules['confidence'][i])
            except:
                consequents1.append(np.nan)
                confidence1.append(np.nan)
            try:
                consequents2.append(list(rules['consequents'][i])[1])
                confidence2.append(rules['confidence'][i])
            except:
                consequents2.append(np.nan)
                confidence2.append(np.nan)
            try:
                consequents3.append(list(rules['consequents'][i])[2])
                confidence3.append(rules['confidence'][i])
            except:
                consequents3.append(np.nan)
                confidence3.append(np.nan)
        else:
            consequents1.append(np.nan)
            consequents2.append(np.nan)
            consequents3.append(np.nan)
            confidence1.append(np.nan)
            confidence2.append(np.nan)
            confidence3.append(np.nan)
        if i == rules.shape[0] - 1:
            i = 0
        i += 1

    # Adiciona a coluna de consequentes na tabela de respostas
    answers['RECOMMENDATION_1'] = consequents1
    answers['RECOMMENDATION_2'] = consequents2
    answers['RECOMMENDATION_3'] = consequents3
    answers['CONFIDENCE_1'] = confidence1
    answers['CONFIDENCE_2'] = confidence2
    answers['CONFIDENCE_3'] = confidence3

    answers = answers.drop(columns=['services'])
    answers.to_csv('recommendation.csv', index=False)


if __name__ == '__main__':
    # Importa a base de dados
    answers = pd.read_csv(
        '/home/maksonvinicio/Documents/GitHub/Data-Science-Projects/Maratona Behind the Code 2021/03_GFT/Data/ANSWERS.csv')
    rules = pd.read_csv(
        '/home/maksonvinicio/Documents/GitHub/Data-Science-Projects/Maratona Behind the Code 2021/03_GFT/Data/rules.csv')
    recommendation(answers, rules)
