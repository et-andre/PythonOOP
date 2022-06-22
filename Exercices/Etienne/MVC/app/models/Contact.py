class Contact:
    def __init__(self, nom, prenom, email, fonction) -> None:
        self.nom      = nom
        self.prenom   = prenom
        self.email    = email
        self.fonction = fonction

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} {self.email} {self.fonction}"
