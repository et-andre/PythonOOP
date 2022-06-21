from flask_wtf          import FlaskForm
from wtforms            import StringField
from wtforms.validators import DataRequired

class Forms(FlaskForm):
    class Meta:
        csrf = False
    
    nom      = StringField("nom"     , validators=[DataRequired()])
    prenom   = StringField("prenom"  )
    email    = StringField("email"   , validators=[DataRequired()])
    fonction = StringField("fonction")
