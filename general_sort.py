import csv, sys, os

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Incorrect arguments.")
    sys.exit()

filename = sys.argv[1]

if len(sys.argv) == 3:
    prefix = sys.argv[2]
else:
    prefix = ''

try:
    with open(filename, 'r') as file:
        data = [line for line in csv.reader(file)]
except FileNotFoundError:
    print("File not found.")
    sys.exit()

data.sort()
with open(filename+'.txt', 'w+') as outfile:
    outfile.write(filename.upper() + '\n\n')
    outfile.write('CODICE                  ||    QUANT.\n')
    outfile.write('='*30 + '\n')
    for line in data:
        line = line[0].split(';')
        if line[1] == 'quant':
            break
        while len(line[0]) < 20:
            line[0] += ' '
        outfile.write(prefix+line[0].upper().replace("'", '') + '    ||    ' + line[1] + '\n')
        outfile.write('_'*30 + '\n')
