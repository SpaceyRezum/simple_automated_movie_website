from __future__ import unicode_literals
# I have read on a forum that my encoding errors could be solved by importing the unicode_literals from Python 3
# so I did and it solved almost all of the codec errors

# coding: utf8


import media
import movie_website

snatch = media.Movie("http://www.imdb.com/title/tt0208092/","https://www.youtube.com/watch?v=ni4tEtuTccc")
inside_jobs = media.Movie("http://www.imdb.com/title/tt1645089/","https://www.youtube.com/watch?v=FzrBurlJUNk")
district_9 = media.Movie("http://www.imdb.com/title/tt1136608/","https://www.youtube.com/watch?v=82s9atP0teY")
coach_carter = media.Movie("http://www.imdb.com/title/tt0393162/","https://www.youtube.com/watch?v=znyAnWUYf2g")
inception = media.Movie("http://www.imdb.com/title/tt1375666/","https://www.youtube.com/watch?v=YoHD9XEInc0")
interstellar = media.Movie("http://www.imdb.com/title/tt0816692/","https://www.youtube.com/watch?v=3WzHXI5HizQ")

movies = [snatch, inside_jobs, district_9, coach_carter, inception, interstellar]

movie_website.open_movies_page(movies)

#for e in movies:
#	print e.imdb_rating

