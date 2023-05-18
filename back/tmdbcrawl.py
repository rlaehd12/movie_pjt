import requests
import json

TMDB_API_KEY = '6aee34be99bb1d1b3fa358b709332b7e'  # .env 파일에서 불러옴.

def get_movie_datas():
    total_data = []

    # 1페이지부터 3페이지까지의 데이터를 가져옴.
    for i in range(1, 4):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                # Movie 모델 필드명에 맞추어 데이터를 저장함.
                data = {
                    "model": "movies.movie",
                    'fields': {
                        'movie_id': movie['id'],
                        'title': movie['title'],
                        'released_date': movie['release_date'],
                        'popularity': movie['popularity'],
                        'vote_avg': movie['vote_average'],
                        'overview': movie['overview'],
                        'poster_path': movie['poster_path'],
                        'genres': movie['genre_ids'],
                        'vote_count': movie['vote_count'],
                    },
                }
                total_data.append(data)

    # print(total_data)


    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=" ", ensure_ascii=False)


#==================================================================================================================================================================

def get_genre_datas():

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko"
    genres = requests.get(request_url).json()
    total_data = []
    for genre in genres['genres']:
        data = {
            "model": "movies.genre",
            'pk': genre['id'],
            'fields': {
                "name": genre['name']
            },
        }
        total_data.append(data)



    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=" ", ensure_ascii=False)

get_movie_datas()
get_genre_datas()