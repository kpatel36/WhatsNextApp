from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')


from .auth_forms import Login_Form, RegisterUserForm
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, logout_user, login_required


@auth.route('/login', methods=['GET','POST'])
def login():
    login_form=Login_Form() # info put into the login form saved to variable login_form
    if request.method == 'POST': # user submitted login form
        if login_form.validate_on_submit(): # user provided valid form information
            # print(login_form.data)
            user = User.query.filter_by(username=login_form.username.data).first()
            if user and check_password_hash(user.password, login_form.password.data):
                login_user(user)
                print(current_user, current_user.__dict__)
                flash(f'Welcome back{current_user.username.data}')
                return redirect (url_for('user_homepage'))
    else:
        # bad form info - let them try again
        flash(f'Login failed, incorrect username or password')
        print('login failed')
        return redirect(url_for('auth.login'))
    return render_template ('login.html', login_form=login_form)

@auth.route('/register', methods=['GET', 'POST'])
def registerUser():
    rform=RegisterUserForm()
    if request.method=='POST':
        if rform.validate_on_submit(): # user provided valid form information
            print(rform.data)
            flash(f"Welcome to the What's Next family {rform.username.data}")
            return redirect (url_for('userprofile'))
        else: # bad form input - reroute to same page again to let them try again
            flash('There was an issue with your registration form - either your username is taken or your passwords did not match. PLease try again')
            return redirect(url_for('auth.register'))
    return render_template('register.html', rform=rform)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"You've been logged out", category='danger')
    return redirect(url_for('home'))