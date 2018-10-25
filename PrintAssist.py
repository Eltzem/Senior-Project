# given list of counters create printable line
from CveBagger import CveBagger


class PrintAssist:

    def __init__(self, cve_list):
        bagger = CveBagger(cve_list)
        count_list = bagger.count_all()[2]
        bagger.get_average()
        bagger.get_deviation()
        a = self.LMH_to_string(count_list[0])
        b = self.NAL_to_string(count_list[1])
        c = self.LMH_to_string(count_list[2])
        d = self.NSM_to_string(count_list[3])
        e = self.NPC_to_string(count_list[4])
        f = self.NPC_to_string(count_list[5])
        g = self.NPC_to_string(count_list[6])
        self.out = ",".join([bagger.get_average(), bagger.get_deviation(), a, b, c, d, e, f, g])

    def NPC_to_string(self, a_counter):
        out = [str(x) for x in [a_counter['NONE'], a_counter['PARTIAL'], a_counter['COMPLETE']]]
        out = ",".join(list(out)).strip("[]")
        return out

    def LMH_to_string(self, a_counter):
        out = [str(x) for x in [a_counter['LOW'], a_counter['MEDIUM'], a_counter['HIGH']]]
        out = ",".join(list(out)).strip("[]")
        return out

    def NSM_to_string(self, a_counter):
        out = [str(x) for x in [a_counter['NONE'], a_counter['SINGLE'], a_counter['MULTIPLE']]]
        out = ",".join(list(out)).strip("[]")
        return out

    def NAL_to_string(self, a_counter):
        out = [str(x) for x in [a_counter['NETWORK'], a_counter['ADJACENT'], a_counter['LOCAL']]]
        out = ",".join(list(out)).strip("[]")
        return out

