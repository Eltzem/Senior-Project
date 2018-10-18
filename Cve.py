
class Cve:

    def __init__(self, score, severity, vector, complexity, authentication, confidentiality, integrity, availability, CWE):
        self.score = score
        self.severity = severity
        self.vector = vector
        self.complexity = complexity
        self.authentication = authentication
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability
        self.CWE = CWE

    def to_string(self):
        return "Score:", self.score, " Severities:", self.severity
