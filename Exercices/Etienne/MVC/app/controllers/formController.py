from app                 import app
from requests            import request
from flask               import render_template, request

from app.models.Contact  import Contact
from app.models.Personne import Personne
from app.forms.Forms     import Forms
from app.services.db     import DB

db = DB()

class CvController:
    @app.route('/form/form', methods=["GET"])
    def contactPage():
        return render_template('form/form.html')

    @app.route('/form/form', methods=["POST"])
    def contactPost():
        form = Forms(request.form)
        if form.validate():
            contact = Contact(form.nom.data, form.prenom.data, form.email.data, form.fonction.data)
            db.insert(form)            
            return render_template('form/form.html', contact = contact)

        return render_template('form/form.html', errors = form.errors)
