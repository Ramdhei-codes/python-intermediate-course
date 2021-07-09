import csv

def read_csv(route):
    dictionary_data = {}

    with open(route, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        dictionary_data = {data[0][i]: data[1][i] for i in range(len(data[0]))}
        
    return dictionary_data



def run():
    route = './cumpleaños.csv'
    read_csv(route)

if __name__ == '__main__':
    run()