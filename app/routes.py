import requests
from flask_login import login_required
from app import app
from flask import render_template, url_for
from .services import get_trending_movies, get_now_playing_movies, get_popular_movies, get_top_rated_tv, get_trending_tv, get_trending_movies2, homepage_tv_show_list
from .forms import PostForm, SearchForm, addtoFavorites

@app.route('/')
def home():
    home_tv_shows = homepage_tv_show_list()
    home_movies_list = get_trending_movies()
    return render_template('homepage.html', home_movies_list = home_movies_list, home_tv_shows=home_tv_shows)


@app.route('/user_profile')
@login_required
def user_profile_page():
    print('should be clicked on to see their saved list and maybe what their following/followers have recommended recently')
    print('user profile page')
    print('should list their saved items, their watchlist/booket list items, link to pages theyre following?')
    return render_template('userprofile.html')

@app.route('/movies')
def movies():
    now_playing_movies= get_now_playing_movies()
    trend_movies = get_trending_movies2()
    pop = get_popular_movies()
    print(trend_movies[1])
    
    print('trying to look at movies page')    
    return render_template('movies.html', now_playing_movies=now_playing_movies,pop=pop, trend_movies=trend_movies)

@app.route('/tv_series')
def tv_series():
    trending_tv= get_trending_tv()
    mi = len(trending_tv)//2
    trending_tv1=trending_tv[:mi]
    trending_tv2=trending_tv[mi:]
    on_the_air = homepage_tv_show_list()
    top_rated_tv = get_top_rated_tv()
    return render_template('tv_series.html',on_the_air=on_the_air, top_rated_tv=top_rated_tv, trending_tv1=trending_tv1,trending_tv2=trending_tv2)

@app.route('/podcasts')
def podcasts():
    print ('trying to look at current popular podcasts page')
    podcast_list_length_6_cards = ['a1','b2','c3','d4','e5','f6']
    return render_template('podcasts.html', podcasts_list_length = podcast_list_length_6_cards)

@app.route('/about')
def about_pg():
    print('accessing the about page')
    return render_template('aboutpage.html')