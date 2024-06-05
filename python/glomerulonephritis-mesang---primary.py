# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"K0A2500","system":"readv2"},{"code":"K032y14","system":"readv2"},{"code":"K032y13","system":"readv2"},{"code":"K019.00","system":"readv2"},{"code":"N03.5","system":"readv2"},{"code":"N01.5","system":"readv2"},{"code":"N04.5","system":"readv2"},{"code":"N05.5","system":"readv2"},{"code":"N03.3","system":"readv2"},{"code":"N00.3","system":"readv2"},{"code":"N02.5","system":"readv2"},{"code":"N02.3","system":"readv2"},{"code":"N00.5","system":"readv2"},{"code":"N01.3","system":"readv2"},{"code":"N04.3","system":"readv2"},{"code":"N05.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('glomerulonephritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["glomerulonephritis-mesang---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["glomerulonephritis-mesang---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["glomerulonephritis-mesang---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
