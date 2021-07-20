import json
import requests
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


def get_movies_detailed_information(movies_lst, genres_list):
    movies_lst = order_by_release_date(movies_lst)
    to_remove = []
    for i in range(len(movies_lst)):
        try:
            one_genre_at_list = False
            movies_lst[i] = dict(movies_lst[i])
            detailed_req = get_summery_by_id(movies_lst[i]['imdb_id'])
            detailed_req = json.loads(json.dumps(detailed_req.json()))
            for j in range(len(detailed_req[movies_lst[i]['title']]['gen'])):
                if detailed_req[movies_lst[i]['title']]['gen'][j]['genre'] in genres_list:
                    one_genre_at_list = True
            if not one_genre_at_list:
                to_remove.append(movies_lst[i])
            else:
                movies_lst[i].update(detailed_req)
        except:
            movies_lst.remove(movies_lst[i])
    for i in range(len(to_remove)):
        movies_lst.remove(to_remove[i])
    return movies_lst[:5]


def order_by_release_date(movie_lst):
    movie_lst = list(movie_lst)
    movie_lst.sort(key=itemgetter('release', 'title'))
    return movie_lst


def coming_soon(genres_list):
    movies = get_movies_base_information()
    movies_dict = json.loads(json.dumps(movies.json()))
    movies_list = list(movies_dict['Movies Upcoming'])
    movies_list = get_movies_detailed_information(movies_list, genres_list)
    return movies_list


def generate_basic_info_dict(movies_list):
    new_dict = {}
    for movie in movies_list:
        new_movie = {'Title': movie['title'],
                     'Release Date': movie['release'],
                     'Description': movie[movie['title']]['description'],
                     'Genres': movie[movie['title']]['gen']}
        new_dict[movie['title']] = new_movie
    return new_dict
    

def lambda_handler(event, context):
    genres_list = set(str(event["queryStringParameters"]["genres"]).split('+'))
    movie_list = coming_soon(genres_list)
    res = json.dumps(generate_basic_info_dict(movie_list))
    return {
        'statusCode': '200',
        'body': res,
        'headers': {
            'Access-Control-Allow-Origin': 'https://master.d3k6fbvlxi2px3.amplifyapp.com', #used for my Aws Amplify App
            'Content-Type': 'application/json',
        },
    }
