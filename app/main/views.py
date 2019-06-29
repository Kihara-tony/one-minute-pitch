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
