def run():
    myList = ['Ram', 'Hernán', 'Camila']
    myDict = {'name': 'Ramdhei', 'lastname': 'López Arcila'}

    super_list = [
        {'name': 'Ramdhei', 'lastname': 'López Arcila'},
        {'name': 'Laura', 'lastname': 'Quiceno Restrepo'},
        {'name': 'Valeria', 'lastname': 'Salazar Cardona'}
    ]

    for element in super_list:
        for key, value in element.items():
            print(key, '=', value)


if __name__ == '__main__':
    run()
