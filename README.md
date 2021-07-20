# New Movies API:
This Lambda uses RapidAPI interface to get the closest 5 movies tagged with genres the user enters (updated to current date).  
The Lambda function gets the movies' information from the free API : https://data-imdb1.p.rapidapi.com/movie/order/upcoming/  
The movies then sorted by release date (primary sort) and alphabetic  
(as a secondary sorting, in case two or more movies being released on the same date).  
The information of <Name, Date, Description, Generes> displayed By Analyzing the json file and specifically displays those details. 
**The project uses AWS Lambda function (using query string parameters) and an Amazon API Gateway endpoint to trigger that function.**  
## Enter a formatted URL in the following way:  
First enter https://lsu71o4toc.execute-api.us-east-2.amazonaws.com/default/coming_soon?genres=  
following by one/some of the following genres (separated by +):  
Action, Horror,  
Adventure, Music,  
Animation, Musical,  
Biography, Mystery,  
Comedy, Romance,  
Crime, Sci Fi,  
Documentary, Short Film,  
Drama, Sport,  
Family, Fantasy, 
Thriller,War,  
History, Western.  
  
**A GET request, For example:**  
If I want to recieve closest 5 action & comedy & Fantasy movies to be on screen, I'll enter the following URL:  
https://lsu71o4toc.execute-api.us-east-2.amazonaws.com/default/coming_soon?genres=Action+Comedy+Fantasy

**The JSON output will be, (updated to today's date:)**  
{  
  "Trollhunters: Rise of the Titans": {  
    "Title": "Trollhunters: Rise of the Titans",  
    "Release Date": "2021-07-21",  
    "Description": "The heroes from the Trollhunters series team-up on an epic adventure to fight the Arcane Order for control over the magic that binds them all.",  
    "Genres": [  
      {  
        "id": 4,  
        "genre": "Adventure"  
      },  
      {  
        "id": 5,  
        "genre": "Family"  
      },  
      {  
        "id": 6,  
        "genre": "Fantasy"  
      },  
      {  
        "id": 8,  
        "genre": "Drama"  
      },  
      {  
        "id": 9,  
        "genre": "Comedy"  
      },  
      {  
        "id": 10,  
        "genre": "Animation"  
      },  
      {  
        "id": 13,  
        "genre": "Action"  
      }  
    ]  
  },  
  "Snake Eyes: G.I. Joe Origins": {  
    "Title": "Snake Eyes: G.I. Joe Origins",  
    "Release Date": "2021-07-22",  
    "Description": "A G.I. Joe spin-off centered around the character of Snake Eyes.",  
    "Genres": [  
      {  
        "id": 4,  
        "genre": "Adventure"  
      },  
      {  
        "id": 6,  
        "genre": "Fantasy"  
      },  
      {  
        "id": 11,  
        "genre": "Sci-Fi"  
      },  
      {  
        "id": 13,  
        "genre": "Action"  
      },  
      {  
        "id": 14,  
        "genre": "Thriller"  
      }  
    ]  
  },  
  "Jungle Cruise": {  
    "Title": "Jungle Cruise",  
    "Release Date": "2021-07-29",  
    "Description": "Based on Disneyland's theme park ride where a small riverboat takes a group of travelers through a jungle filled with dangerous animals and reptiles but with   a supernatural element.",  
    "Genres": [  
      {  
        "id": 4,  
        "genre": "Adventure"  
      },  
      {  
        "id": 5,  
        "genre": "Family"  
      },  
      {  
        "id": 6,  
        "genre": "Fantasy"  
      },  
      {  
        "id": 9,  
        "genre": "Comedy"  
      },  
      {  
        "id": 13,  
        "genre": "Action"  
      }  
    ]  
  },  
  **.**  
  **.**  
  **.**  
  "Hotel Transylvania: Transformania": {  
    "Title": "Hotel Transylvania: Transformania",  
    "Release Date": "2021-08-05",  
    "Description": "Plot unknown. Fourth installment of the 'Hotel Transylvania' franchise.",  
    "Genres": [  
      {  
        "id": 4,  
        "genre": "Adventure"  
      },  
      {  
        "id": 5,  
        "genre": "Family"  
      },  
      {  
        "id": 6,  
        "genre": "Fantasy"  
      },  
      {  
        "id": 9,  
        "genre": "Comedy"  
      },  
      {  
        "id": 10,  
        "genre": "Animation"  
      },  
      {  
        "id": 28,  
        "genre": "Horror"  
      }  
    ]  
  }  
}  
  
(*be notice that the quntity of the movies returned depends on movies' release dates in those specific genres.)
