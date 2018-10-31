import os


class SeverityAssembler:

    def __init__(self):

        Top16_CWE_list = ["CWE-119", "CWE-264", "CWE-89", "CWE-20", "CWE-284", "CWE-416", "CWE-399", "CWE-77",
                          "CWE-787", "CWE-125", "CWE-426", "CWE-287", "CWE-78", "CWE-190", "CWE-502", "CWE-798"]
        LMH = "Low" + "," + "Medium" + "," + "High" + ","
        Vectors = "Network" + "," + "Adjacent Network" + "," + "Local" + ","
        NSM = "None" + "," + "Single" + "," + "Multiple" + ","
        NPC = "None" + "," + "Partial" + "," + "Complete" + ","

        for file in Top16_CWE_list:
            with open(os.path.abspath('highSeverityCWE/datasets/' + file + "-dataset.csv"), 'w', newline='') as out_file:
                # Writing header
                out_file.write(
                    "Year" + "," + "average score" + "," + "deviation" + ",," + "severities" + ",,," + "vectors" + ",,," + "complexities")
                out_file.write(
                    ",,," + "authentication" + ",,," + "confidentiality" + ",,," + "integrity" + ",,," + "availability\n")

                out_file.write(",,," + LMH + Vectors + LMH + NSM + NPC + NPC + NPC + "\n")
                out_file.close()

        for filename in os.listdir('highSeverityCWE/'):
            # Don't want to access directories
            if(filename[-4:] == ".csv"):
                # filename end open datasets file with same name
                with open('highSeverityCWE/' + filename, 'r', newline='') as in_file:
                    with open('highSeverityCWE/datasets/' + filename[5:-4] + "-dataset.csv", 'a', newline='') as out_file:
                        out_file.write(filename[:4] + "," + in_file.read() + "\n")