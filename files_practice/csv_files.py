import csv

with open('./examples/employees.txt', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count+=1
        print(f'\t{row["name"]} works as a {row["role"]} and was born in {row["birthday month"]}')
        line_count+=1


