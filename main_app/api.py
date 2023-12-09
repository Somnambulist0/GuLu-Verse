import requests
import time

def fetch_movies(api_key, page=1):
    #Fetches movies from TMDb API with extended information for classification. 
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'page': page,
        'vote_count.gte': 0,  # Minimum number of votes to consider
        'vote_average.gte': 0,  # Minimum rating to consider
        'include_adult': 'false',
        'include_video': 'false',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results'], response.json()['total_pages']
    else:
        return [], 0

def fetch_movie_details(api_key, movie_basic_info):
    movie_id = movie_basic_info['id']
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': api_key,
        'append_to_response': 'credits'  
    }
    response = requests.get(details_url, params=params)
    if response.status_code == 200:
        movie_details = response.json()
        movie_basic_info.update(movie_details)
        return movie_basic_info
    else:
        return None

def fetch_all_movies(api_key, total_pages=10):
    all_movies_details = []
    for page in range(1, total_pages + 1):
        movies, _ = fetch_movies(api_key, page)
        for movie_basic_info in movies:
            detailed_info = fetch_movie_details(api_key, movie_basic_info)
            if detailed_info:
                all_movies_details.append(detailed_info)
            time.sleep(0.5) 
    return all_movies_details


def fetch_genres(api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()['genres']
        return {genre['id']: genre['name'] for genre in genres}
    else:
        return {}
    


