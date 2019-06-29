from flask_wtf import FlaskForm
from wtforms.validators import Required,Email
from wtforms import SubmitField, TextAreaField, StringField,ValidationError
from ..models import User
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you that you may like to share.', validators=[Required()])
    submit = SubmitField('Submit')