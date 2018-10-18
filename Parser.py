import json
import csv
from Cve import Cve
from CveBagger import CveBagger
from pprint import pprint


def parse(afile):
    cve_list = []

    with open(afile, encoding="utf-8") as file:
        data = json.load(file)
        cve_items = data.get('CVE_Items')

        # Beginning to parse here...
        for item in cve_items:

            # Here is where we're grabbing CWE type and place them in a dict w/ incremented values
            cve = item.get('cve')
            problemtype = cve.get('problemtype')
            if problemtype is not None:
                problemtype_data = problemtype.get('problemtype_data')[0].get('description')
                if len(problemtype_data) > 0:
                    cwe = problemtype_data[0]
                    cwe_value = cwe.get('value')

                    # grabbing impact
                    impact = item.get('impact')

                    # Grabbing cvssv2 metrics and placing them in lists
                    baseMetricV2 = impact.get('baseMetricV2')
                    severity = baseMetricV2['severity']

                    if baseMetricV2 is not None:
                        cvssV2 = baseMetricV2.get('cvssV2')

                        a = cvssV2['baseScore']
                        b = cvssV2['accessVector']
                        c = cvssV2['accessComplexity']
                        d = cvssV2['authentication']
                        e = cvssV2['confidentialityImpact']
                        f = cvssV2['integrityImpact']
                        g = cvssV2['availabilityImpact']
                        cve_list.append(Cve(a, severity, b, c, d, e, f, g, cwe_value))
    a = CveBagger(cve_list)
    print(a.count("severity").values())
    print(list(a.count("severity").values())[0])
    print(list(a.count("severity").keys())[0])
    for item in a.count_all()[2]:
        print(list(item.values()))


'''

        # Counting the # of each score in the lists
        list_of_complexities = Counter(list_of_complexities)
        list_of_authentication = Counter(list_of_authentication)
        list_of_confidentiality = Counter(list_of_confidentiality)
        list_of_intergrities = Counter(list_of_intergrities)
        list_of_availabilities = Counter(list_of_availabilities)

        # Prepping to write
        with open(afile[:-4] + "csv", 'w', newline='') as csv_file:
            severities = str((list_of_severities['LOW'], list_of_severities['MEDIUM'], list_of_severities['HIGH']))
            vectors = str((list_of_vectors['NETWORK'], list_of_vectors['ADJACENT_NETWORK'], list_of_vectors['LOCAL']))
            complexities = str((list_of_complexities['LOW'], list_of_complexities['MEDIUM'], list_of_complexities['HIGH']))
            authentication = str((list_of_authentication['NONE'], list_of_authentication['SINGLE'], list_of_authentication['MULTIPLE']))
            confidentiality = str((list_of_confidentiality['NONE'], list_of_confidentiality['PARTIAL'], list_of_confidentiality['COMPLETE']))
            integrity = str((list_of_intergrities['NONE'], list_of_intergrities['PARTIAL'], list_of_intergrities['COMPLETE']))
            availability = str((list_of_availabilities['NONE'], list_of_availabilities['PARTIAL'], list_of_availabilities['COMPLETE']))

            # oof
            out2 = "," + authentication + "," + confidentiality + "," + integrity + "," + availability
            out = afile[20:-5] + "," + average_score + "," + deviation + "," + severities + "," + vectors + "," + complexities
            out = out + out2
            out = out.replace("(", "").replace(")", "").replace(" ", "")
            csv_file.write(out)

        # Load Used CWEs into dictionary
        with open("CWE metrics/import.csv", 'r') as cwe_metric_file:
            reader = csv.reader(cwe_metric_file)
            cwe_dict = dict((rows[0], rows[1]) for rows in reader)

            # we write this to vectors directory instead.
            with open("vectors/" + afile[9:-5] + "_cwedata.csv", 'w', encoding="utf-8", newline = '') as cwe_file:
                for item in top_ten_cwe:
                    cwe_file.write(str(item[0]).strip('()') + ",")
                    cwe_file.write(str(item[1]).strip('()'))

                    # If we have a name for the CWE we list it
                    if item[1] in cwe_dict.keys():
                        cwe_file.write(","+ str(cwe_dict.get(item[1])).strip('()') + "\n")
                    else:
                        cwe_file.write("\n")
'''