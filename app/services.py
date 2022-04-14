from ...env import tmdb_api_key
import requests as r
# trending movies
def get_trending_movies():
    trending_movies=[]
    trending_movies_response = r.get(f'https://api.themoviedb.org/3/trending/movie/week?api_key={tmdb_api_key}')
    if trending_movies_response == 200:
        trending_this_week_movie_api = trending_movies_response.json()
        # print(len(trending_this_week_movie_api['results']))
        for x in trending_this_week_movie_api['results']:
            # print (f" movie title: {x['original_title']}")
            # print (f" movie overview: {x['overview']}")
            tm = {'trending_movie_title': x['original_title'], 'trending_movie_overview':x['overview']}
            tm_copy=tm.copy()
            trending_movies.append(tm_copy)
        print(trending_movies)
    else:
        print(trending_movies,trending_movies_response.status_code)
    return trending_movies

    .env