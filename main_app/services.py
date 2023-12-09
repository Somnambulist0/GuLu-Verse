import random

#movie_recommendation_logic
def movie_recommendation_logic(mood, classic, noisy, reality, alone, movies):
    print(mood, classic, noisy, reality, alone)
    filtered_movies = []
    print(f"Total movies: {len(movies)}")  
    for movie in movies:
        classification = movie.classification
        # movie_types = classification['type'].split(', ')
        movie_types = [genre.strip() for genre in classification['type'].split(',')]
        # is_popular = classification['popularity'] == "Popular"
        is_classic = classification['release_date_category'] == "Classic"

        meets_mood = (mood == 'Sad' and ('Comedy' in movie_types or 'Animation' in movie_types)) or (mood == 'Happy')
        meets_classic = (classic == 'Classic' and is_classic) or (classic == 'Freshness' and not is_classic)
        meets_noisy = (noisy == 'Quiet' and any(genre in ['History', 'Family', 'Documentary', 'Romance', 'Music'] for genre in movie_types)) or \
                (noisy == 'Noisy' and not all(genre in ['History', 'Family', 'Documentary', 'Romance', 'Music'] for genre in movie_types))
    
        meets_reality = (reality == 'reality' and any(genre in ['History', 'Family', 'Documentary'] for genre in movie_types)) or \
                        (reality == 'imagination' and not all(genre in ['History', 'Family', 'Documentary'] for genre in movie_types))

        meets_alone = (alone == 'else' and any(genre in ['Romance', 'Family', 'Horror'] for genre in movie_types)) or (alone == 'alone')

        # print(f"Movie: {movie.title}")
        if movie.title == "Leo":
            print(f"  Genres: {movie_types}, Is Alone: {meets_alone}")
        # print(f"  Meets Mood: {meets_mood}")
        # print(f"  Meets Niche: {meets_niche}")
        # print(f"  Meets Noisy: {meets_noisy}")
        # print(f"  Meets Reality: {meets_reality}")
        # print(f"  Meets Alone: {meets_alone}")
        # break
        if meets_mood and meets_classic and meets_noisy and meets_reality and meets_alone:
            filtered_movies.append(movie)
            # if len(filtered_movies) >= 5:
            #     break  
    print(f"Filtered movies: {len(filtered_movies)}")
    return random.sample(filtered_movies, min(3, len(filtered_movies)))








    