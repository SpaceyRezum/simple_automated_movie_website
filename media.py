from __future__ import unicode_literals
# My encoding errors could be solved by importing the unicode_literals from Python 3
# so I did and it solved almost all of the codec errors
# coding: utf8

from bs4 import BeautifulSoup
import webbrowser
import urllib
import re

class Movie():
	'''This class is a way to store movie data'''

	VALID_RATINGS = ["G", "PG", "PG13", "R"]

	def __init__(self, imdb_url, trailer_youtube):
		# In the init function, I decided to use Beautifulsoup library to scrape the movie's official IMDB url for meta data.
		# Since trailer videos are not always available on IMDB, I kept adding the youtube url manually.
		soup = BeautifulSoup(urllib.urlopen(imdb_url), "html.parser") # creates "soup" an instance of the BeautifulSoup class
		self.title = re.sub(r'(\([0-9]{4}\)|\-.{1,})','',soup.find(class_="title_wrapper").h1.get_text())
		# In self.title, I used the soup.find to get the original movie
		# title which came with the release date (and sometimes some unnecessary details after a "-"), hence the re.sub() to
		# remove it all.
		self.release_year = re.sub(r'\(|\)','',soup.find(id="titleYear").get_text())
		# In self.release_year, the year came with two parenthesis so I removed them with re.sub()
		self.director = soup.find(class_="credit_summary_item").span.get_text().strip()
		self.length = soup.find(class_="subtext").time.get_text().strip()
		self.imdb_rating = soup.find(class_="ratingValue").span.get_text()
		self.storyline = soup.find(class_="summary_text").get_text().strip()
		self.poster_image_url = soup.find(class_="poster").img['src']
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)



