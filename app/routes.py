from flask_login import login_required
from app import app
from flask import render_template, url_for

@app.route('/')
def home():
    # should display trending media in each category?
    # pull random ones or display new/popular ones?
    print('hello')
    return render_template('homepage.html')

@app.route('/user_newsfeed')
def user_homepage():
    print('user logged in and sees all their recommendations and newsfeed')
#     # 1. side nav/second nav banner on top - discover more (links to movies, pods, books, tv)
#     # 2. newsfeed for other users this user is following
#     # 3. 
    return render_template('user_homepage.html')

@app.route('/user_profile')
@login_required
def user_profile_page():
    print('should be clicked on to see their saved list and maybe what their following/followers have recommended recently')
    print('user profile page')
    print('should list their saved items, their watchlist/booket list items, link to pages theyre following?')
    return render_template('userprofile.html')

@app.route('/movies')
def movies():
    movie_list_length_8_cards = ['a1','b2','c3','d4','e5','f6','g7','h8']
    print('trying to look at movies page')
    return render_template('movies.html', movie_list_length = movie_list_length_8_cards)

@app.route('/tv_series')
def tv_series():
    tv_list_length_10_cards = ['a1','b2','c3','d4','e5','f6','g7','h8','i9','j10']
    print ('trying to look at current popular tv_series page')
    return render_template('tv_series.html',TV_list_length=tv_list_length_10_cards)


@app.route('/podcasts')
def podcasts():
    print ('trying to look at current popular podcasts page')
    podcast_list_length_8_cards = ['a1','b2','c3','d4','e5','f6','g7','h8']
    return render_template('podcasts.html', podcasts_list_length = podcast_list_length_8_cards)

@app.route('/books')
def books():
    print ('trying to look at current popular books page')
    return render_template('books.html')

@app.route('/about')
def about_pg():
    print('accessing the about page')
    return render_template('aboutpage.html')

# @app.route('/music')
# def music():
#     print ('trying to look at current popular music')
#     return render_template('music.html')