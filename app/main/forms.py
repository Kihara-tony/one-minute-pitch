from flask_wtf import FlaskForm
from wtforms.validators import Required,Email
from wtforms import SubmitField, TextAreaField, StringField,ValidationError
from ..models import User
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about you that you may like to share.', validators=[Required()])
    submit = SubmitField('Submit')
class GeneralForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')
class PitchForm(FlaskForm):
    pitch_title = StringField('Title', validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Write Your Pitch!')
class CommentForm(FlaskForm):
    comment_content = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Comment')
class GeneralReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')
