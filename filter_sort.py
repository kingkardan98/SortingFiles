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

        codes = line[0].split('=')
        for code in codes:
            while len(line[0]) < 20:
                line[0] += ' '
        quants = line[1].split('+')
        while len(codes) != len(quants):
            quants.append('0')
        isEl = False
        for quant in quants:
            if 'el' in quant:
                isEl = True
        
        if isEl:
            for i in range(len(quants)):
                if not ' el' in quants[i]:
                    quants[i] += ' el' 
        
        for i in range(len(codes)):
            if i == 0:
                outfile.write(prefix + codes[i].upper().replace("'", '') + '    ||    ' + quants[i] + '\n')
            else:
                outfile.write('↪ ' + prefix + codes[i].upper().replace("'", '') + '  ||    ' + quants[i] + '\n')
            outfile.write('_'*30 + '\n')
