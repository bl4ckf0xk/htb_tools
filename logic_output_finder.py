import csv

file_path = "input.csv"
output = []

with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)

        for i in reader:
                first_and = int(i[0]) & int(i[1])
                second_and = int(i[2]) & int(i[3])

                or_out = first_and | second_and
                output.append(str(or_out))
output = ''.join(output)
print(output)
