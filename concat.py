filenames = ['./csv/weather_106_sorted.csv',
            './csv/data_airq.csv']
MISSING_DATA = "-999"
def check(shardDate, lines):
    for line in lines:
        if shardDate in line:
            return line.strip()
    return 0
with open(filenames[0]) as infile:
    file0_lines = infile.readlines()
    file0_line_no = len(file0_lines)  # Number of line in pm2.5 file
with open(filenames[1]) as infile:
    file1_lines = infile.readlines()
    file1_line_no = len(file1_lines)
with open('./csv/data.csv', 'w') as outfile:
    print("WRITING WEATHER DATA")
    for i in range(file0_line_no):
        file0_line = file0_lines[i].strip()
        outfile.write(file0_line)
        sharedDate = ",".join(file0_line.split(",")[:4]) + "," # get minute,hour,day,month,
        lineToWrite = check(sharedDate, file1_lines)
        if lineToWrite:
            outfile.write(
                "," + ','.join(lineToWrite.split(",")[4:]))
            outfile.write("\n")
        else:
            outfile.write("," + MISSING_DATA + "," + MISSING_DATA + "," +
                        MISSING_DATA + "," + MISSING_DATA + "," + MISSING_DATA)
            outfile.write("\n")
    print("WRITING WEATHER DATA DONE!")
    print("WRITING AIR QUALITY DATA")
    for i in range(file1_line_no):
        file1_line = file1_lines[i].strip()
        sharedDate = ",".join(file1_line.split(",")[:4]) + "," # get minute,hour,day,month,
        lineToWrite = check(sharedDate, file0_lines)
        if lineToWrite:
            continue
        else:
            outfile.write(",".join(file1_line.split(",")[:4]))
            outfile.write("," + MISSING_DATA + "," + MISSING_DATA + "," +
                        MISSING_DATA + "," + MISSING_DATA + "," + MISSING_DATA + ",")
            outfile.write(",".join(file1_line.split(",")[4:]))
            outfile.write("\n")
    print("WRITING AIR QUALITY DATA DONE!")
    print("LOOK UP RESULT AT data.csv file")

       
