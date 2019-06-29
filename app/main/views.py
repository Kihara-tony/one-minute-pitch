from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from . import main 
from flask_login import login_required, current_user
from .forms import UpdateProfile, GeneralForm, GeneralReviewForm
from .. import db
from sqlalchemy import func
from ..models import User,  Upvote, Downvote
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Welcome to The Pitch app'

    return render_template('index.html', title=title)
@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname=user.username))

        return render_template('profile/update.html', form=form)
@main.route('/',methods = ['GET', 'POST'])

def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)


    title = 'One Minute Pitch'
    return render_template('index.html', title = title, pitch = pitch,  likes=likes, dislikes=dislikes)


