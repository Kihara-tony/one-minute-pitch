from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from ..models import User
from .forms import LoginForm, RegistrationForm
from . import auth
from flask_login import login_user, logout_user, login_required
from .. import db