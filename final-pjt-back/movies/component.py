from xml.etree.ElementInclude import include
import requests
from .models import Movie, Similar


# 인기순 영화 정보 저장
def movie_API(page):
    Movie.objects.all().delete()
    for i in range(1,page+1):
        url = 'https://api.themoviedb.org/3'
        path = '/movie/now_playing'
        params = {
            'api_key': '143a27aa8ba75a3d662d1f05a4e1b4f9',
            'language': 'ko',
            'region': 'KR',
            'page': i,
        }
        movies = requests.get(url + path+'?',params=params).json()
        
        for movie in movies['results']:
            instance = Movie.objects.create(
            title = movie['title'],
            release_date = movie['release_date'],
            popularity = movie['popularity'],
            overview = movie['overview'],
            poster_path = movie['poster_path'],
            movie_id = movie['id'],
            genre_id = movie['genre_ids'][0],
            )
            instance.save()
    return movies

# 비슷한 영화 정보 저장
def get_similar_movie_API(movie_id):
    url = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/similar'
    params = {
        'api_key': '143a27aa8ba75a3d662d1f05a4e1b4f9',
        'language': 'ko',
        'region': 'KR',
    }
    movies = requests.get(url + path+'?',params=params).json()
    
    Similar.objects.all().delete()
    for movie in movies['results']:
        instance = Similar.objects.create(
        title = movie['title'],
        release_date = movie['release_date'],
        popularity = movie['popularity'],
        overview = movie['overview'],
        poster_path = movie['poster_path'],
        movie_id = movie['id'],
        genre_id = movie['genre_ids'][0],
        )
        instance.save()
    return movies



# 장르별 영화 API
def genre_API(genre_id,page):
    Movie.objects.all().delete()
    for i in range(1,page+1):
        url = 'https://api.themoviedb.org/3'
        path = '/discover/movie'
        params = {
            'api_key': '143a27aa8ba75a3d662d1f05a4e1b4f9',
            'language': 'ko',
            'region': 'KR',
            'with_genres': genre_id,
            'page' : i
        }
        movies = requests.get(url + path+'?',params=params).json()
        
        for movie in movies['results']:
            instance = Movie.objects.create(
            title = movie['title'],
            release_date = movie['release_date'],
            popularity = movie['popularity'],
            overview = movie['overview'],
            poster_path = movie['poster_path'],
            movie_id = movie['id'],
            genre_id = movie['genre_ids'][0],
            )
            instance.save()
    return movies

# 영화 검색 기능
def search_API(movie_title):
    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '143a27aa8ba75a3d662d1f05a4e1b4f9',
        'language': 'ko',
        'region': 'KR',
        'query': movie_title,
        'include_adult': True,
    }
    movies = requests.get(url + path+'?',params=params).json()
    
    Movie.objects.all().delete()
    for movie in movies['results']:
        instance = Movie.objects.create(
        title = movie['title'],
        release_date = movie['release_date'],
        popularity = movie['popularity'],
        overview = movie['overview'],
        poster_path = movie['poster_path'],
        movie_id = movie['id'],
        )
        instance.save()
    return movies

