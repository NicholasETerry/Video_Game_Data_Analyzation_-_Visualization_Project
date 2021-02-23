import json
from types import SimpleNamespace
import requests, json



# JSON within a string
import requests

json_data = '{"name": "David", "age": 26}'

# Convert JSON string to dict
json_data_dict = json.loads(json_data)
# Convert JSON string into Python Object
person = json.loads(json_data, object_hook=lambda d: SimpleNamespace(**d))
# Can now use dot notation to access values
print(person.name)
# Output: David
# Type of object is 'types.SimpleNamespace'
print(type(person))
# Output: <class 'types.SimpleNamespace'>
# Access values via their key
print(json_data_dict['name'])
# Output: David


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def person_decoder(obj):
        return Person(obj['name'], obj['age'])


# THIS WOULD BE A DIFFERENT FILE FROM CLASS PERSON

# JSON within a string
json_data = '{ "Name": "David", "age": 26}'
# Convert JSON string to dictionary
json_data_dict = json.loads(json_data)
# Call static decoder method on Person class
person = Person.person_decoded(json_data_dict)
# Access values using dot notation
print(person.name)
# Output: David
# Type of object is 'Person'
print(type(person))
# Output: <class '__main__.Person'>

# requests - Example GET

# Making a GET call
response = requests.get('https://localhost:44325/api/movie')
# Prints the entire JSON API response in a string format
print(response.content)
# Output: (Long string of json)
# Using .json() to instead receive the API response in a dictionary format
movies = response.json()
# Using keys to access a value in our dictionary
print(movies[0]['title'])
# Output: The Departed

# requests - Example POST

movie = {'title': 'Groundhog Day', 'director': 'Harold Ramis', 'genre': 'Comedy'}
# Making POST call. json=movie specifies we are sending json
response = requests.post('https://localhost:44325/api/movie', json=movie)
# Prints the entire JSON API response in a string format
print(response.content)
# Output: {"movieId":4, "title": "Groundhog Day", "director": "Harold Ramis", "genre": "Comedy"}'
# Using .json() to instead receive the API response in a dictionary format
created_movie = response.json()
# Using keys to access a value in out dictionary
print(created_movie['title'])
# Output: Groundhog Day

# Adding Headers to a HTTP Request

# Create dict of header key value pairs
headers = {'auth-token': '...example'}
# Pass header dict into hte headers parameter
response = requests.get('https://localhost:44325/api/movie', headers=headers)
# Print the status code of the API response
print(response.status_code)


# Adding Parameters to a HTTP Request

# Create dict of parameter key value pairs
payload = {'key1': 'value1', 'key2': 'value2'}
# Pass payload dict into the params parameter
response = requests.get('http://localhost:44325/api/movie', params=payload)
# Print the status code of the API response
print(response.status_code)


# GET Request with JSON decoding

response = requests.get('https://localhost:44325/api/movie')
movies = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

for movie in movies:
    print(movie.title)
# Output:
# The Departed:
# The Dark Knight:
# Inception:
# Pineapple Express:
# Die Hard:
# Groundhog Day:
