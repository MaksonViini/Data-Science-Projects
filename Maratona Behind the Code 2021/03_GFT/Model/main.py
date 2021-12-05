import pandas as pd
def recommendation(answers, rules) -> pd.DataFrame:
    """[Function to recommend a service]

    Args:
        answers ([dataframe]): [Dataframe with the answers of the user]
        rules ([type]): [Dataframe with the rules of the association rules]
    """

    # Verifica todas as marcacoes de answer e retorna uma lista de lista com todas as marcacoes
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

    # Verifica todas as marcacoes dos consequentes e retorna uma lista de lista com todas as marcacoes
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
            consequents1.append(list(rules['consequents'][i])[0])
            confidence1.append(rules['confidence'][i])
            try:
                consequents2.append(list(rules['consequents'][i])[1])
                consequents3.append(list(rules['consequents'][i])[2])
                confidence2.append(rules['confidence'][i])
                confidence3.append(rules['confidence'][i])
            except:
                consequents2.append(None)
                consequents3.append(None)
                confidence2.append(None)
                confidence3.append(None)
        else:
            consequents1.append(None)
            consequents2.append(None)
            consequents3.append(None)
            confidence1.append(None)
            confidence2.append(None)
            confidence3.append(None)
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
