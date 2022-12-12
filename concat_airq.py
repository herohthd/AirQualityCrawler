filenames = ['./csv/pm2_5.csv',
             './csv/co.csv',
             './csv/no2.csv',
             './csv/o3.csv',
             './csv/so2.csv']
MISSING_DATA = "-999"
def check(shardDate, lines):
    for line in lines:
        if shardDate in line:
            return line.strip()
    return 0
with open('./csv/data_airq.csv', 'w') as outfile:
    with open(filenames[0]) as infile:
        line_no = len(infile.readlines())  # Number of line in pm2.5 file
    with open('./csv/data_airq.csv', 'w') as outfile:
        for i in range(line_no):
            for file in filenames:
                with open(file) as infile:
                    infileLines = infile.readlines()
                    if file == filenames[0]:
                        infileLine = infileLines[i].strip()
                        outfile.write(infileLine)
                        sharedDate = ",".join(infileLine.split(",")[:4])
                    else:
                        lineToWrite = check(sharedDate, infileLines)
                        print(lineToWrite)
                        if lineToWrite:
                            if file == filenames[-1]:
                                outfile.write("," + lineToWrite.split(",")[-1] + "\n")
                            else:
                                outfile.write("," + lineToWrite.split(",")[-1])
                        else:
                            if file == filenames[-1]:
                                outfile.write("," + MISSING_DATA + "\n")
                            else:
                                outfile.write("," + MISSING_DATA)
                            continue