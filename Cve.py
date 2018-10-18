
class Cve:

    def __init__(self, score, severity, vector, complexity, authentication, confidentiality, integrity, availability, ):
        self.score = score
        self.severity = severity
        self.vector = vector
        self.complexity = complexity
        self.authentication = authentication
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability
        self.CWE = None

    def to_string(self):
        return "Score:", self.score, " Severities:", self.severity
