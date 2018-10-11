import json
import numpy as np
from collections import Counter
from pprint import pprint
import csv


def parse(afile):
    with open(afile, encoding="utf-8") as file:
        data = json.load(file)
        cve_items = data.get('CVE_Items')

        # Distribution of Vulns
        total_cve_items = 0       # Get number of Vulns
        list_of_scores = []
        summed_score = 0          # Average Vuln Value
        list_of_severities = []   # Dist by Severity level
        list_of_vectors = []      # Access Vector
        list_of_complexities = [] # Access Complexity
        cwe_count = {}             # Dict containing CWE occurrence rate

        # Beginning to parse here...
        for item in cve_items:

            # Here is where we're grabbing CWE type and place them in a dict w/ incremented values
            cve = item.get('cve')
            problemtype = cve.get('problemtype')
            if problemtype is not None:
                problemtype_data = problemtype.get('problemtype_data')[0].get('description')
                if(len(problemtype_data) > 0):
                    cwe = problemtype_data[0]
                    cwe_value = cwe.get('value')
                    if cwe_value in cwe_count:
                        cwe_count[cwe_value] = cwe_count.setdefault(cwe_value) + 1
                    else:
                        cwe_count[cwe_value] = 1

            # grabbing impact
            impact = item.get('impact')

            # Grabbing cvssv2 metrics and placing them in lists
            baseMetricV2 = impact.get('baseMetricV2')
            if baseMetricV2 is not None:
                cvssV2 = baseMetricV2.get('cvssV2')

                list_of_severities.append(baseMetricV2.get('severity'))
                list_of_scores.append(cvssV2['baseScore'])
                list_of_vectors.append(cvssV2['accessVector'])
                list_of_complexities.append(cvssV2['accessComplexity'])

                total_cve_items += 1
                summed_score += cvssV2['baseScore']

        print("Total Number of Entries", total_cve_items)
        # print("List of Scores", listOfScores)

        # Calculating average score & deviation
        average_score = summed_score / total_cve_items
        average_score = "{0:.2f}".format(average_score)
        deviation = "{0:.2f}".format(np.std(list_of_scores, dtype=np.float64))

        # Prepping top 10 CWE vectors to be written
        inverse = [(value, key) for key, value in cwe_count.items()]
        top_ten_cwe = sorted(inverse,reverse=True) #[0:25]

        # Counting the # of each score in the lists
        list_of_severities = Counter(list_of_severities)
        list_of_vectors = Counter(list_of_vectors)
        list_of_complexities = Counter(list_of_complexities)

        # Prepping to write
        with open(afile[:-4] + "csv",'w',newline = '') as csv_file:
            severities = str((list_of_severities['LOW'], list_of_severities['MEDIUM'], list_of_severities['HIGH']))
            vectors = str((list_of_vectors['NETWORK'], list_of_vectors['ADJACENT_NETWORK'], list_of_vectors['LOCAL']))
            complexities = str((list_of_complexities['LOW'], list_of_complexities['MEDIUM'], list_of_complexities['HIGH']))

            out = afile[20:-5] + "," + average_score + "," + deviation + "," + severities + "," + vectors + "," + complexities
            out = out.replace("(","").replace(")","").replace(" ","")
            csv_file.write(out)

        # Load Used CWEs into dictionary
        with open("CWE metrics/import.csv", 'r') as cwe_metric_file:
            reader = csv.reader(cwe_metric_file)
            cwe_dict = dict((rows[0], rows[1]) for rows in reader)

            # we write this to vectors directory instead.
            with open("vectors/" + afile[9:-5] + "_cwedata.csv",'w',newline = '') as cwe_file:
                for item in top_ten_cwe:
                    cwe_file.write(str(item[0]).strip('()') + ",")
                    cwe_file.write(str(item[1]).strip('()') + "\n")
                    #print(item[1][4:])
                    if((item[1][4:] in cwe_dict.values())):
                        print("hit")
