from sklearn.impute import KNNImputer
from sklearn.naive_bayes import CategoricalNB
from numpy import nan
from pandas import read_csv, DataFrame

# path to the diabetes datafile, modify befor use
data_path = "/home/vincent/Programing/github/main/python_programing/Info180/oblig_4/diabetes.csv"

dataset = read_csv(data_path, header=None)

def nearest_neighbor(dataset:DataFrame):
    """normalizes the dataset, identifies witch rows have empty values,
    searches the dataset for nearest neighbour (moste similar row),
    and tries to find the most common non zero value in the group of
    nearest neighbour to fill in the empty value,

    Args:
        dataset (DataFrame): a DataFrame generated with the pandas module for python

    Returns:
        Dataframe: the transformed data
    """

    # to store the sizes that every column was normelized by
    sizes = {}

    data = dataset.copy()

    # replaces values in column index 1, 2, 3, 4, 5, 6, 7 with nan; the 0s in 1 and 8 are not missing values but simply the value of 0
    data[[1,2,3,4,5,6,7]] = data[[1,2,3,4,5,6,7]].replace(0, nan)

    # normalize every number to a number between 0 and 1
    for column in data:
        size = data[column].max()
        sizes[column] = size
        data[column] = [x/size for x in data[column]]

    # initializes the KNNImputer class that fills every empty input
    # in the entire dataframe with the nearest neighbor method
    imputer = KNNImputer()
    data = imputer.fit_transform(data)

    data = DataFrame(data)

    # de-normalizes the values in the dataframe
    for column in data:
        size = sizes[column]
        if column != 6 and column != 5:
            data[column] = [round(x*size) for x in data[column]]
        else:
            data[column] = [round(x*size, 4) for x in data[column]]

    return data

def make_dict(min_numb:int, max_numb:int, numb_groups:int = 5)->dict:
    """tar imot to tall og lager en dict der alle tall mellom de to tallene er knyttet til et tall mellom 0 og 5, 
    dvs 0, 1, 2, 3, 4
    som en form for grupering etter størelse

    Args:
        min_numb (int): minste tallet
        max_numb (int): største tallet
        numb_groups (int, optional): antall grupper. Defaults to 5.

    Returns:
        dict: alle tallene mellom min og max knyttet til et tal på antal grupper
    """
    result = {}

    # the numbers as a percentage of the largest number and the number it self
    numb_as_prc = [(x/max_numb, x) for x in range(min_numb, max_numb+1)]

    # the thresholds to enter each group based on numb_groups and the given number
    thresholds = [((1/numb_groups)*(x+1), x) for x in range(0, numb_groups)]

    for i in numb_as_prc:
        prc, num = i
        for j in thresholds:
            threshold, group = j
            # if the number as a percentage is less than the threshold add "group" to the "result" 
            # dictionary with the key "num" and dont test for the rest of the thresholds
            if prc <= threshold:
                result[num] = group
                break

    return result

def naiv_bayes(dataset:DataFrame):
    data = dataset.copy()

    for column in data:
        # i collone 5 og 6 er det desimal tall som min funksjon ikke er lagd for å hondtere
        if column != 5 and column != 6:
            mult_factor = 1

        if column == 5 or column == 6:
            match column:
                case 5:
                    mult_factor = 10
                case 6:
                    mult_factor = 1000
        if column == 8:
            continue

        column_max = round(data[column].max()*mult_factor)
        column_min = round(data[column].min()*mult_factor)
        relevant_dict = make_dict(column_min, column_max)
        des_relevant_dict = {}

        for key in relevant_dict:
            des_relevant_dict[key/mult_factor] = relevant_dict[key]
        
        relevant_dict = des_relevant_dict      

        data[column] = data[column].replace(relevant_dict)

    categories = range(0, 768)

    clf = CategoricalNB()
    clf.fit(data, categories)

    return clf

neighbor = nearest_neighbor(dataset)
bays = naiv_bayes(dataset)
data = dataset[[0, 1, 2, 3, 4, 5, 6, 7, 8]]

print(bays.predict(data))