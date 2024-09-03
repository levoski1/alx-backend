



import csv

class load():
    def __init__(self, dataset_csv):
        self.__datasetcsv = dataset_csv
        self.__dataset = None

    def dataset(self):
        with open(self.__datasetcsv, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            dataset = [read for read in reader]
            return dataset

get = input('Name of your csv file: ')
obj = load(get)

print(obj.dataset())
