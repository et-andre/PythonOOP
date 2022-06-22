from app                 import conn

from app.forms.Forms     import Forms
from app.models.Personne import Personne
from app.models.Contact  import Contact

class DB:
    def __init__(self) -> None:
        pass

    def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM personne")
        pers = []
        for p in cur.fetchall():
            pers.append(per(p[0], p[1], p[2], p[3], p[4]))

        return pers

    def findOneById(self, id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM personne WHERE pk = {id}")
        pers = cur.fetchone()        

        return Personne(pers[0], pers[1], pers[2], pers[3], pers[4])

    def findOneByName(self, nom):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM personne WHERE nom = '{nom}'")
        pers = cur.fetchone()        

        return Personne(pers[0], pers[1], pers[2], pers[3], pers[4])

    def insert(self, data: Forms):
        cur = conn.cursor()
        cur.execute("INSERT INTO personne(nom, prenom, email, fonction) VALUES('" + str(data.nom.data     ) + "', " +
                                                                              "'" + str(data.prenom.data  ) + "', " +
                                                                              "'" + str(data.email.data   ) + "', " +
                                                                              "'" + str(data.fonction.data) + "')")
        conn.commit()

        return self.findOneByName(data.nom.data)
