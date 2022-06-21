from app                import app
from requests           import request
from flask              import render_template, request
from app.models.Contact import Contact

from app.models.Personne   import Personne

class CvController:
    @app.route('/form/form', methods=["GET"])
    def contactPage():
        return render_template('cv/contact.html')

    @app.route('/form/form', methods=["POST"])
    def contactPost():
        form = Form(request.form)
        if form.validate():
            contact = Contact(form.nom.data, form.prenom.data, form.email.data, form.fonction.data)
            return render_template('cv/contact.html', contact = contact)

        return render_template('cv/contact.html', errors = form.errors)
