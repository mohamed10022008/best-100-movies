import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
best_movies = response.text
beauty_soup = BeautifulSoup(best_movies, "html.parser")
name_of_movie_non_formated = [movie.getText() for movie in beauty_soup.find_all("h3", "title")]
for n in range(len(name_of_movie_non_formated)-1, 0, -1):
    with open("movies.text", "a") as movies:
        movies.write(name_of_movie_non_formated[n] + "\n")
