import requests
import json
from operator import itemgetter


def get_movies_base_information():
    url = "https://data-imdb1.p.rapidapi.com/movie/order/upcoming/"
    # generes = {'Action': 'Action', 'Drama': 'Drama'}
    headers = \
        {
            'x-rapidapi-key': '536f37d223msh3a1b16637225a9fp12499djsn62c02055bd2e',
            'x-rapidapi-host': 'data-imdb1.p.rapidapi.com'
        }
    response = requests.request("GET", url, headers=headers)  # params=generes)
    return response


def get_summery_by_id(movie_id):
    url = "https://data-imdb1.p.rapidapi.com/movie/id/" + movie_id + '/'
    headers = \
        {
            'x-rapidapi-key': '536f37d223msh3a1b16637225a9fp12499djsn62c02055bd2e',
            'x-rapidapi-host': 'data-imdb1.p.rapidapi.com'
        }
    response = requests.request("GET", url, headers=headers)
    return response


def get_movies_detailed_information(movies_lst, genres_set):
    movies_lst = order_by_release_date(movies_lst)
    to_remove = []
    for i in range(len(movies_lst)):
        try:
            one_genre_at_list = False
            movies_lst[i] = dict(movies_lst[i])
            detailed_req = get_summery_by_id(movies_lst[i]['imdb_id'])
            detailed_req = json.loads(json.dumps(detailed_req.json()))
            for j in range(len(detailed_req[movies_lst[i]['title']]['gen'])):
                if detailed_req[movies_lst[i]['title']]['gen'][j]['genre'] in genres_set:
                    one_genre_at_list = True
            if not one_genre_at_list:
                for j in range(len(detailed_req[movies_lst[i]['title']]['keywords'])):
                    if detailed_req[movies_lst[i]['title']]['keywords'][j]['keyword'] in genres_set:
                        one_genre_at_list = True
            if not one_genre_at_list:
                to_remove.append(movies_lst[i])
            else:
                movies_lst[i].update(detailed_req)
        except:
            movies_lst.remove(movies_lst[i])
    for i in range(len(to_remove)):
        movies_lst.remove(to_remove[i])
    return movies_lst


def get_genres_from_user():
    genre_list = []
    print("Enter as much as you like from the following genres (or write 'all' for all genres):")
    print('Action       Horror\n'
          'Adventure    Music\n'
          'Animation    Musical\n'
          'Biography    Mystery\n'
          'Comedy       Romance\n'
          'Crime        Sci-Fi\n'
          'Documentary  Short Film\n'
          'Drama        Sport\n'
          'Family       Superhero\n'
          'Fantasy      Thriller\n'
          'Film-Noir    War\n'
          'History      Western\n')
    genres_str = input()
    genre_list = genres_str.split(' ')
    if 'Film-Noir' in genre_list:
        genre_list.remove('Film-Noir')
        genre_list.append('Film Noir')
    return set(genre_list)


def order_by_release_date(movie_lst):
    movie_lst = list(movie_lst)
    movie_lst.sort(key=itemgetter('release', 'title'))
    return movie_lst


movies = get_movies_base_information()
movies_dict = json.loads(json.dumps(movies.json()))
movies_list = list(movies_dict['Movies Upcoming'])
Genres_set = get_genres_from_user()
movies_list = get_movies_detailed_information(movies_list, Genres_set)

for single_movie in movies_list:
    title = single_movie['title']
    print(f"Title: {title}")
    print(f"Release Date: {single_movie['release']}")
    print(f"Description: {single_movie[title]['description']}")
    print("Genres:")
    for genre in single_movie[title]['gen']:
        print(f"{genre['genre']}")
