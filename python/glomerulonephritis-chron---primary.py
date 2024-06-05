# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"K02y200","system":"readv2"},{"code":"K02y000","system":"readv2"},{"code":"K02..00","system":"readv2"},{"code":"K0A3.00","system":"readv2"},{"code":"K0A3000","system":"readv2"},{"code":"K0A3200","system":"readv2"},{"code":"K021.00","system":"readv2"},{"code":"K02yz00","system":"readv2"},{"code":"K02y.00","system":"readv2"},{"code":"K023.00","system":"readv2"},{"code":"K02z.00","system":"readv2"},{"code":"K0A3600","system":"readv2"},{"code":"K02y300","system":"readv2"},{"code":"K020.00","system":"readv2"},{"code":"N03.7","system":"readv2"},{"code":"N03.1","system":"readv2"},{"code":"N03.4","system":"readv2"},{"code":"N03.8","system":"readv2"},{"code":"N03.6","system":"readv2"},{"code":"N03.0","system":"readv2"},{"code":"N03.2","system":"readv2"},{"code":"N03.9","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('glomerulonephritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["glomerulonephritis-chron---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["glomerulonephritis-chron---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["glomerulonephritis-chron---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
