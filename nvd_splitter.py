with open("nvd.txt",'r',encoding="utf8") as infile:
    with open("nvdout.csv",'w',encoding="utf8") as outfile:
        for line in infile:
            outfile.write(line.replace(" 	",",").replace("\"",""))