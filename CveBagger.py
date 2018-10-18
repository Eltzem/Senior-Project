from Cve import Cve
from collections import Counter
import numpy as np


class CveBagger:

    def __init__(self, cve_list):
        self.cve_list = cve_list
        self.cve_attributes = ("severity", "vector", "complexity", "authentication", "confidentiality", "integrity", "availability", "CWE")

    # returns tuple w/ average, stdev, and list of counter objects
    def count_all(self):
        counter_list = []
        for item in self.cve_attributes:
            counter_list.append(self.count(item))

        return self.get_average(), self.get_deviation(), counter_list

    def count(self, attribute):
        return Counter(getattr(cve, attribute) for cve in self.cve_list)

    def get_average(self):
        total_score = 0
        for item in self.cve_list:
            total_score += item.score
        average_score = total_score / len(self.cve_list)
        return "{0:.2f}".format(average_score)

    def get_deviation(self):
        score_list = []
        for item in self.cve_list:
            score_list.append(getattr(item, "score"))
        deviation = "{0:.2f}".format(np.std(score_list, dtype=np.float64))
        return deviation
