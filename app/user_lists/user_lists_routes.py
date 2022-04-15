from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import db, User#, Post;

user_lists = Blueprint('user_lists',__name__,template_folder='user_lists_templates', url_prefix='/user_profiles')

@user_lists.route('/<string:username>')
def userProfile(username):
    user= User.query.filter_by(username=username).first()
    if user:
        print('user exists')
        p = str('user exists')
    else:
        print('no user exists')
        p = str('user does not exist, therefor post and lists can not exist')
    return render_template('userprofile.html', user=user, p=p)


@user_lists.route('/findusers')
def findUsers():
    # if the user is logged in:
    if current_user.is_authenticated:
        # query db User table to get all users not the currently logged in user
        allusers_list = User.query.filter(User.id!=current_user.id).all()
    else:
        # if no user signed in, get all users
        allusers_list = User.query.all()
    return render_template('findusers.html', users=allusers_list)

@user_lists.route('/newsfeed')
def newsfeed():
    if current_user.is_authenticated:
        # posts=current_user.followed_posts()
        print(current_user.followed)
    else: 
        # posts = Post.query.order_by(Post.timestamp.desc()).all()
        print('no one is signed in')
    return render_template('user_homepage.html')


@user_lists.route('/follow/<string:uid>')
@login_required
def follow(uid):
    u=User.query.get(uid)
    current_user.follow(u)
    flash(f'You are now following @{u.username}', 'info')
    return redirect(url_for('user_lists.userProfile', username=u.username))



@user_lists.route('/unfollow/<string:uid>')
@login_required
def unfollow(uid):
    u=User.query.get(uid)
    current_user.unfollow(u)
    flash(f'You are no longer following @{u.username}', 'info')
    return redirect(url_for('user_lists.userProfile', username=u.username))