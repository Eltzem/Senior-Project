import json
import numpy as np
from collections import Counter


def parse(afile):
    with open(afile, encoding="utf-8") as file:
        data = json.load(file)
        cve_items = data.get('CVE_Items')

        # Distribution of Vulns
        totalCveItems = 0 # Get number of Vulns
        listOfScores = []
        summedScore = 0   # Average Vuln Value
        listOfSeverities = [] # Dist by Severity level
        listOfVectors = [] # Access Vector
        listOfComplexities = [] # Access Complexity

        for item in cve_items:
            # grabbing impact
            impact = item.get('impact')

            baseMetricV2 = impact.get('baseMetricV2')
            if baseMetricV2 is not None:
                cvssV2 = baseMetricV2.get('cvssV2')

                listOfSeverities.append(baseMetricV2.get('severity'))
                listOfScores.append(cvssV2['baseScore'])
                listOfVectors.append(cvssV2['accessVector'])
                listOfComplexities.append(cvssV2['accessComplexity'])

                totalCveItems += 1
                summedScore += cvssV2['baseScore']



        print("Total Number of Entries",totalCveItems)
        # print("List of Scores", listOfScores)

        averageScore = summedScore / totalCveItems
        stringout = "{0:.2f}".format(averageScore)
        print("The Average base score is: ", stringout)
        print("std: ", "{0:.2f}".format(np.std(listOfScores, dtype=np.float64)))

        print("Counter Severities",Counter(listOfSeverities))
        print("Counter Vectors",Counter(listOfVectors))
        print("Counter Complexities",Counter(listOfComplexities))