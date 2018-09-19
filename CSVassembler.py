import os

with open("dataset.csv", 'w', newline='') as out_file:
    # Writing header
    out_file.write("Year" + "," + "average score" + "," + "deviation" + ",," + "severities" + ",,," + "vectors" + ",,," + "complexities\n")

    for filename in os.listdir('datasets/'):
        if filename[-4:] == ".csv":
            with open("datasets/" + filename,"r") as in_file:
                out_file.write(in_file.read() + "\n")
                print("Writing from: ",filename)
