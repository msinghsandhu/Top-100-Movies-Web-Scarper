from bs4 import BeautifulSoup
import requests

MOVIES_URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

Movie_Name = []
Movie_Number = []

response = requests.get(MOVIES_URL)
movies_website= response.text
soup = BeautifulSoup(movies_website,'html.parser')


movie_name2 = soup.select('span h2')
N = len(movie_name2)-1

while N!=0:
  Movie_Name.append(movie_name2[N].text.split(')',maxsplit=1)[1].strip())
  Movie_Number.append(movie_name2[N].text.split(')',maxsplit=1)[0].strip())
  N-=1


with open('movies.txt','w') as file:
  for i in range(0,len(Movie_Name)):
    file.write(f'{Movie_Number[i]}. {Movie_Name[i]}\n')