from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')


from .auth_forms import Login_Form, RegisterUserForm
from app.models import User, db
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
                flash(f'Welcome back {current_user.username}', category='success')
                return redirect (url_for('user_lists.newsfeed'))
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
            try:
                # initialize instance of a new User in User database
                new_user = User(rform.username.data, rform.email.data, rform.password.data,rform.first_name.data, rform.last_name.data)
                # add them to the database and commit change to database
                db.session.add(new_user)
                db.session.commit()
                # successful registration - redirect user to user_homepage (or explore page)
                print(f'{rform.username.data} user created successfully')
            except: 
                flash('Username or E-mail is taken. Please try something else.', category='warning')
                return redirect (url_for('auth.registerUser'))
            # log in user
            login_user(new_user)
            flash(f"Welcome to the What's Next family {rform.username.data}", category='success')
            return redirect (url_for('user_profile_page'))
            
        else: # bad form input - reroute to same page again to let them try again
            flash('There was an issue with your registration - either your passwords did not match or you provided an improper email/username. Please try again', category='info')
            return redirect(url_for('auth.registerUser'))
    return render_template('register.html', rform=rform)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f"You've been logged out", category='secondary')
    return redirect(url_for('auth.login'))