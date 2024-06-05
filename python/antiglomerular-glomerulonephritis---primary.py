# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"K0A0100","system":"readv2"},{"code":"K0A0000","system":"readv2"},{"code":"K0A2000","system":"readv2"},{"code":"K014.00","system":"readv2"},{"code":"K015.00","system":"readv2"},{"code":"K0A..00","system":"readv2"},{"code":"K0A2100","system":"readv2"},{"code":"N04.0","system":"readv2"},{"code":"N04.1","system":"readv2"},{"code":"N01.0","system":"readv2"},{"code":"N02.0","system":"readv2"},{"code":"N01.1","system":"readv2"},{"code":"N02.1","system":"readv2"},{"code":"N05.1","system":"readv2"},{"code":"N00.0","system":"readv2"},{"code":"N05.0","system":"readv2"},{"code":"N00.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('glomerulonephritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["antiglomerular-glomerulonephritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["antiglomerular-glomerulonephritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["antiglomerular-glomerulonephritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
