import os
import requests as r





def genre_list():
    genres=[]
    tmdb_api_key = os.environ.get('tmdb_api_key')
    get_genres_list = r.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={tmdb_api_key}&language=en-US")
    if get_genres_list.status_code==200:
        get_genres_list=get_genres_list.json()
        print(get_genres_list)
    else:
        print(get_genres_list.status_code)
    return get_genres_list



def get_now_playing_movies():
    now_playing=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    now_playing_movies_response = r.get(f"https://api.themoviedb.org/3/movie/now_playing?api_key={tmdb_api_key}&language=en-US&page=1")
    if now_playing_movies_response.status_code== 200:
        now_playing_movies=now_playing_movies_response.json()
        for x in now_playing_movies['results']:
            now_playing.append([x].copy())
        print(now_playing)
    else:
        print(now_playing_movies_response.status_code)
        now_playing.append(now_playing_movies_response)
    return now_playing

def get_popular_movies():
    pop_movies=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    popmovies_response = r.get(f"https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api_key}&language=en-US&page=1")
    if popmovies_response.status_code== 200:
        popmovies=popmovies_response.json()
        for x in popmovies['results']:
            pop_movies.append([x].copy())
    else:
        print(popmovies_response.status_code)
        pop_movies.append(popmovies_response)
    return pop_movies


def get_trending_movies():
    trending_movies=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    trending_movies_response = r.get(f'https://api.themoviedb.org/3/trending/movie/day?api_key={tmdb_api_key}')
    if trending_movies_response.status_code == 200:
        trending_this_week_movie_api = trending_movies_response.json()
        for x in trending_this_week_movie_api['results']:
            trending_movies.append([x].copy())
    else:
        print(trending_movies,trending_movies_response.status_code)
    return trending_movies


def get_trending_movies2():
    trending_movies2_whole_dict=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    trending_movies_response = r.get(f'https://api.themoviedb.org/3/trending/movie/week?api_key={tmdb_api_key}')
    if trending_movies_response.status_code == 200:
        trending_this_week_movie_api = trending_movies_response.json()
        for x in trending_this_week_movie_api['results']:
            trending_movies2_whole_dict.append([x].copy())
    else:
        print(trending_movies2_whole_dict,trending_movies_response.status_code)
    return trending_movies2_whole_dict

def get_trending_tv():
    trending_tv=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    trending_tv_response = r.get(f'https://api.themoviedb.org/3/trending/tv/week?api_key={tmdb_api_key}&language=en-US')
    if trending_tv_response.status_code == 200:
        trending_this_week_tv = trending_tv_response.json()
        for x in trending_this_week_tv['results']:
            trending_tv.append([x].copy())
        print(trending_tv)
    else:
        print(trending_tv,trending_tv_response.status_code)
    return trending_tv

def get_top_rated_tv():
    top_rated_TV=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    top_ratedTV = r.get(f'https://api.themoviedb.org/3/tv/top_rated?api_key={tmdb_api_key}&language=en-US')
    if top_ratedTV.status_code == 200:
        top_ratedTV = top_ratedTV.json()
        for x in top_ratedTV['results']:
            top_rated_TV.append([x].copy())
    else:
        print(top_ratedTV,top_ratedTV.status_code)
    return top_rated_TV

def homepage_tv_show_list():
    hp_tv_list = []
    tmdb_api_key=os.environ.get('tmdb_api_key')
    tv_listings = r.get(f'https://api.themoviedb.org/3/tv/on_the_air?api_key={tmdb_api_key}&language=en-US&page=1')
    if tv_listings.status_code == 200:
        tv_listings = tv_listings.json()
        for x in tv_listings['results']:
            hp_tv_list.append([x].copy())
    else:
        print(tv_listings, tv_listings.status_code)
    return hp_tv_list

def latest_tv():
    latest_tv_list = []
    tmdb_api_key=os.environ.get('tmdb_api_key')
    tv_listings = r.get(f'https://api.themoviedb.org/3/tv/on_the_air?api_key={tmdb_api_key}&language=en-US&page=1')
    if tv_listings.status_code == 200:
        tv_listings = tv_listings.json()
        for x in tv_listings['results']:
            latest_tv_list.append([x].copy())
    else:
        print(tv_listings, tv_listings.status_code)
    return latest_tv_list
