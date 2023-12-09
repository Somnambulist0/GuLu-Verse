from .models import Movie  
from datetime import datetime

def classify_movie(movie_data,genres_map):
    # classification
    genre_names = [genres_map.get(genre_id, 'Unknown') for genre_id in movie_data.get('genre_ids', [])]
    classification = {
        'type': ', '.join(genre_names),
        'rating': 'High' if movie_data['vote_average'] >= 7 else 'Low',
        'popularity': 'Popular' if movie_data['popularity'] > 50 else 'Less Popular',
        'release_date_category': 'New' if datetime.strptime(movie_data['release_date'], '%Y-%m-%d').year > 2010 else 'Classic'
    }
    return classification


def save_movie_data(movies_data, genres_map):
    for movie_data in movies_data:
        # analyze movie_data
        classification = classify_movie(movie_data, genres_map)

        # info
        title = movie_data['title']
        genre_ids = movie_data['genre_ids'] 
        overview = movie_data['overview']
        vote_average = movie_data['vote_average']
        release_date = movie_data.get('release_date', '')
        cast = ", ".join([member['name'] for member in movie_data.get('credits', {}).get('cast', [])][:5]) 
        poster_path = movie_data.get('poster_path', '')

        # save movie_data to database
        Movie.objects.create(
            title=title,
            genre=','.join(map(str, genre_ids)),
            classification=classification,
            overview=overview,
            vote_average=vote_average,
            release_date=datetime.strptime(release_date, '%Y-%m-%d') if release_date else None,
            cast=cast,  
            poster_path=poster_path 
        )

