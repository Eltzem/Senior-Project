import os


class CSVassembler:

    def __init__(self):
        with open("dataset.csv", 'w', newline='') as out_file:
            # Writing header
            out_file.write("Year" + "," + "average score" + "," + "deviation" + ",," + "severities" + ",,," + "vectors" + ",,," + "complexities")
            out_file.write(",,," + "authentication" + ",,," + "confidentiality" + ",,," + "integrity" + ",,," + "availability\n")
            LMH = "Low" + "," + "Medium" + "," + "High" + ","
            Vectors = "Network" + "," + "Adjacent Network" + "," + "Local" + ","
            NSM = "None" + "," + "Single" + "," + "Multiple" + ","
            NPC = "None" + "," + "Partial" + "," + "Complete" + ","
            out_file.write(",,," + LMH + Vectors + LMH + NSM + NPC + NPC + NPC + "\n")

            for filename in os.listdir('datasets/'):
                if filename[-4:] == ".csv":
                    with open("datasets/" + filename,"r") as in_file:
                        out_file.write(in_file.read() + "\n")
                        print("Writing from: ",filename)
