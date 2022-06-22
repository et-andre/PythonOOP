class Experience:
    def __init__(self, date, nom) -> None:
        self.date = date
        self.nom  = nom

class Personne:
    def __init__(self, pk, prenom, nom, email, fonction) -> None:
        self.pk          = pk
        self.prenom      = prenom
        self.nom         = nom
        self.email       = email
        self.fonction    = fonction
        self.experiences = []
        self.skills      = []
        self.formations  = []

    def addExperience(self, date, nom):
        self.experiences.append(Experience(date, nom))

    def addSkills(self, txt):
        self.skills.append(txt)

    def addFormation(self, txt):
        self.formations.append(txt)