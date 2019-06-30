from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import SubmitField, TextAreaField, StringField,ValidationError
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you that you may like to share.', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch_title = StringField('Title', validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment_content = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Comment')
