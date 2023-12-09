from django.core.management.base import BaseCommand
from main_app.load_data import save_movie_data  
from main_app.api import fetch_all_movies,fetch_genres
from main_app.api_keys import TMDB_API_KEY

class Command(BaseCommand):
    help = 'Loads movies data from TMDb API into the database'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--pages', type=int, default=10, help='Number of pages to fetch from TMDb API')

    def handle(self, *args, **options):
        api_key = TMDB_API_KEY
        total_pages = options['pages']
        movies_data = fetch_all_movies(api_key, total_pages=total_pages)
        genres_map = fetch_genres(TMDB_API_KEY)
        save_movie_data(movies_data, genres_map)
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {total_pages} pages of movies data into database'))