import os
import requests as r
# trending movies
def get_trending_movies():
    trending_movies=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    trending_movies_response = r.get(f'https://api.themoviedb.org/3/trending/movie/week?api_key={tmdb_api_key}')
    if trending_movies_response.status_code == 200:
        trending_this_week_movie_api = trending_movies_response.json()
        # print(len(trending_this_week_movie_api['results']))
        for x in trending_this_week_movie_api['results']:
            # print (f" movie title: {x['original_title']}")
            # print (f" movie overview: {x['overview']}")
            tm = {'trending_movie_title': x['original_title'], 'trending_movie_overview':x['overview'], 'pic_link':x["poster_path"]}
            tm_copy=tm.copy()
            trending_movies.append(tm_copy)
        print(trending_movies)
    else:
        print(trending_movies,trending_movies_response.status_code)
    return trending_movies



def get_trending_tv():
    trending_tv=[]
    tmdb_api_key=os.environ.get('tmdb_api_key')
    trending_tv_response = r.get(f'https://api.themoviedb.org/3/trending/tv/week?api_key={tmdb_api_key}')
    if trending_tv_response.status_code == 200:
        trending_this_week_tv = trending_tv_response.json()
        for x in trending_this_week_tv['results']:
    #         # print (f" movie title: {x['original_title']}")
    #         # print (f" movie overview: {x['overview']}")
            ttv = {'trending_tv_title': x['original_name'], 'trending_tv_overview':x['overview'], 'pic_path':x["poster_path"]}
            ttv_copy=ttv.copy()
            trending_tv.append(ttv_copy)
        print(trending_tv)
    else:
        print(trending_tv,trending_tv_response.status_code)
    return trending_tv