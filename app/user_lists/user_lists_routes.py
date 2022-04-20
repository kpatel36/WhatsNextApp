import json
from webbrowser import get
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user, login_required
from sqlalchemy import func

from app.services import genre_list, get_now_playing_movies, latest_tv
from ..forms import SearchForm, addtoFavorites,PostForm
from app.models import db, User, followers, load_user, MovieFaves, MovieWatchlist, TVSeriesFavorites, TVWatchlist, PodcastFavorites, PodcastListenList, BooketList, BookFavorites,Posts;

user_lists = Blueprint('user_lists',__name__,template_folder='user_lists_templates', url_prefix='/user_profiles')

@user_lists.route('/<string:username>', methods=['GET', 'POST'])
def userProfile(username):
    user= User.query.filter_by(username=username).first()
    if user: # if user exists, query Post Table for their posts and display them
        posts = Posts.query.filter_by(user_id=user.id).order_by(Posts.timestamp.desc()).all()
        movie_fave_list = MovieFaves.query.filter_by(user_id=user.id).order_by(MovieFaves.timestamp.desc()).all()
        movie_watchlist = MovieWatchlist.query.filter_by(user_id=user.id).order_by(MovieWatchlist.timestamp.desc()).all()
        tv_fave_list = TVSeriesFavorites.query.filter_by(user_id=user.id).order_by(TVSeriesFavorites.timestamp.desc()).all()
        tv_watchlist = TVWatchlist.query.filter_by(user_id=user.id).order_by(TVWatchlist.timestamp.desc()).all()
        # book_faves_list = BookFavorites.query.filter_by(user_id=user.id).order_by(BookFavorites.timestamp.desc()).all()
        # books_to_read_list = BooketList.query.filter_by(user_id=user.id).order_by(BooketList.timestamp.desc()).all()
        # podcast_faves_list = PodcastFavorites.query.filter_by(user_id=user.id).order_by(PodcastFavorites.timestamp.desc()).all()
        # podcasts_to_listen_list = PodcastListenList.filter_by(user_id=user.id).order_by(PodcastListenList.timestamp.desc()).all()
    else: #user does not exist
        return (render_template('userprofile.html', user=None, posts=None, movie_fave_list=None, movie_watchlist=None, tv_fave_list=None, tv_watchlist=None))    
    form = PostForm()
    if request.method =='POST' and current_user.is_authenticated:
        if current_user.id ==user.id and form.validate_on_submit():
            addingPost = Posts()
            addingPost.body = form.postbody.data
            addingPost.user_id = current_user.id
            db.session.add(addingPost)
            db.session.commit()
            flash('Post successfully added to your feed', 'info')
            return redirect(url_for('user_lists.userProfile', username=current_user.username))
        else:
            return jsonify({'This is not your account.': 'Please create your own account to make a comment'}),403
    return render_template('userprofile.html', user=user, posts=posts, form=form, movie_fave_list=movie_fave_list, movie_watchlist=movie_watchlist, tv_fave_list=tv_fave_list, tv_watchlist=tv_watchlist)


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
    latest_tv_list=latest_tv()
    new_release_m=get_now_playing_movies()
    genres=genre_list()
    return render_template('user_homepage.html',latest_tv_list=latest_tv_list, new_release_movies=new_release_m)


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

@user_lists.route('/addtoMovieFaves/<string:movie_title>')
@login_required
def addToMovie_Faves(movie_title):
    if current_user.is_authenticated:
        adding_movie=MovieFaves()
        adding_movie.movie_title = movie_title
        adding_movie.user_id = current_user.id
        db.session.add(adding_movie)
        db.session.commit()
        flash(f'Successfully added to {movie_title} your movie favorites', 'info')
        print(adding_movie)
    else:
        flash('Something went wrong. Please try adding that title again')
        print('error - nothing added')
    return redirect(request.referrer)

@user_lists.route('/deleteFromMovieFaves/<int:mfaves_id>')
@login_required
def delFromMovie_Faves(mfaves_id):
    remove_item = MovieFaves.query.get(mfaves_id)
    if current_user.id == remove_item.user_id:
        db.session.delete(remove_item)
        db.session.commit()
        flash('Movie removed from your favorites list', 'info')
        return redirect(request.referrer)
    return jsonify ({'Not a place for you', 'buddy'}, 403)

@user_lists.route('/addtoMovieWatchlist:<string:movie_title>')
@login_required
def addToMovie_Watchlist(movie_title):
    if current_user.is_authenticated:
        adding_movie=MovieWatchlist()
        adding_movie.movie_title = movie_title
        adding_movie.user_id = current_user.id
        db.session.add(adding_movie)
        db.session.commit()
        flash('Successfully added to your watchlist', 'info')
        print(adding_movie)
    else:
        flash('Something went wrong. Please try adding that title again')
        print('error - nothing added')
    return redirect(request.referrer)
    

@user_lists.route('/deleteFromMovieWatchlist/<int:mwatchlist_id>')
@login_required
def delFromMovie_Watchlist(mwatchlist_id):
    remove_item = MovieWatchlist.query.get(mwatchlist_id)
    if current_user.id == remove_item.user_id:
        db.session.delete(remove_item)
        db.session.commit()
        flash(f'{remove_item.movie_title} removed from your watchlist list', 'info')
        return redirect(url_for('user_lists.viewUserMovieWatchlist',username=current_user.username))
    return jsonify ({'Not a place for you', 'buddy'}, 403)

@user_lists.route('/movie-favorites/<string:username>')
def viewUserMovieFavorites(username): 
    user= User.query.filter_by(username=username).first()
    userFaveMovies = MovieFaves.query.filter_by(user_id=user.id).order_by(MovieFaves.timestamp.desc()).all()
    print(userFaveMovies)
    return render_template('userMovieFavorites.html', user=user, users_fave_movies=userFaveMovies)

@user_lists.route('/movie-watchlist/<string:username>')
def viewUserMovieWatchlist(username):
    user= User.query.filter_by(username=username).first()
    userWatchlistMovies = MovieWatchlist.query.filter_by(user_id=user.id).order_by(MovieWatchlist.timestamp.desc()).all()
    return render_template('userMovieWatchlist.html', user=user, users_movies_watchlist=userWatchlistMovies)

@user_lists.route('/addtoTVFaves/<string:show_title>')
@login_required
def addToTV_Faves(show_title):
    if current_user.is_authenticated:
        adding_tv=TVSeriesFavorites()
        adding_tv.show_title = show_title
        adding_tv.user_id = current_user.id
        db.session.add(adding_tv)
        db.session.commit()
        flash(f'Successfully added {show_title} to your show favorites', 'info')
        print(adding_tv.__dict__)
    else:
        flash('Something went wrong. Please try adding that title again')
        print('error - nothing added')
    return redirect(request.referrer)

@user_lists.route('/deleteFromTVFaves/<int:tvfaves_id>')
@login_required
def delFromTV_Faves(tvfaves_id):
    remove_item = TVSeriesFavorites.query.get(tvfaves_id)
    if current_user.id == remove_item.user_id:
        db.session.delete(remove_item)
        db.session.commit()
        flash(f'{remove_item.series_title} removed from your favorites list', 'info')
        return redirect(url_for('user_lists.viewUserTVFavorites',username=current_user.username))
    return jsonify ({'Not a place for you', 'buddy'}, 403)

@user_lists.route('/addtoTVWatchlist:<string:show_title>')
@login_required
def addToTV_Watchlist(show_title):
    if current_user.is_authenticated:
        adding_tv=TVWatchlist()
        adding_tv.show_title = show_title
        adding_tv.user_id = current_user.id
        db.session.add(adding_tv)
        db.session.commit()
        flash(f'Successfully added {show_title} to your watchlist', 'info')
        print(adding_tv.__dict__)
    else:
        flash('Something went wrong. Please try adding that title again')
        print('error - nothing added')
    return redirect(request.referrer)
    

@user_lists.route('/deleteFromTVWatchlist/<int:tvwatchlist_id>')
@login_required
def delFromTV_Watchlist(tvwatchlist_id):
    remove_item = TVWatchlist.query.get(tvwatchlist_id)
    if current_user.id == remove_item.user_id:
        db.session.delete(remove_item)
        db.session.commit()
        flash(f'{remove_item.show_title} removed from your TV watchlist', 'info')
        return redirect(url_for('user_lists.viewUserTVWatchlist',username=current_user.username))
    return jsonify ({'Not a place for you', 'buddy'}, 403)

@user_lists.route('/TV-favorites/<string:username>')
def viewUserTVFavorites(username): 
    user= User.query.filter_by(username=username).first()
    userFaveTV = TVSeriesFavorites.query.filter_by(user_id=user.id).order_by(TVSeriesFavorites.timestamp.desc()).all()
    print([show.show_title for show in userFaveTV])
    return render_template('userTVfaves.html', user=user, users_fave_tv=userFaveTV)

@user_lists.route('/TV-watchlist/<string:username>')
def viewUserTVWatchlist(username):
    user= User.query.filter_by(username=username).first()
    userWatchlistTV = TVWatchlist.query.filter_by(user_id=user.id).order_by(TVWatchlist.timestamp.desc()).all()
    return render_template('userTVwatchlist.html', user=user, users_TV_watchlist=userWatchlistTV)