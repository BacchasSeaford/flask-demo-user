from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, IntegerField, FileField
from wtforms.validators import InputRequired

class profileForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    age = IntegerField('age', validators=[InputRequired()])
    gender = SelectField('gender', choices=[('male','female','other')])
    biography = TextAreaField('biography', validators=[InputRequired()])
    file = FileField('file', validators=[InputRequired()])
