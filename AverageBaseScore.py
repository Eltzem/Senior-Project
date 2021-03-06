import json
import numpy as np
from pprint import pprint


with open('Datasets/nvdcve-1.0-2017.json', encoding="utf-8") as file:
    # Load data into dictionary
    data = json.load(file)

    # First dict has mostly header crap, we want the data
    cve_items = data.get('CVE_Items')

    # This one is a list ??
    # pprint(type(cve_items))

    # Make our iterables
    count = 0
    total = 0
    totalCveItems = 0
    listOfScores = []

    # Each key in this dictionary contains an individual cve
    for item in cve_items:
        # grabbing impact
        impact = item.get('impact')
        totalCveItems += 1

        # Here's where we start to run into some issues, some of these are actually nonetypes
        # Might be some formatting issues?
        baseMetricV2 = impact.get('baseMetricV2')

        if baseMetricV2 is not None:
            cvssV2 = baseMetricV2.get('cvssV2')
            #pprint(cvssV2['baseScore'])
            total += cvssV2['baseScore']
            listOfScores.append(cvssV2['baseScore'])
            count += 1
        '''
        else:
            pprint(item)
        '''
    out = total / count

    print("total items:", totalCveItems)
    print("Valid items: ", count)
    print("Invalid items: ", totalCveItems - count)
    print("percent invalid: ", (totalCveItems - count) / totalCveItems * 100)

    stringout = "{0:.2f}".format(out)
    print("The Average base score is: ", stringout)
    print("std: ", np.std(listOfScores, dtype=np.float64))

    file.close()


