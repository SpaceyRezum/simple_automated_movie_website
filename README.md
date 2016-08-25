Intro

In this project, I worked mostly with Python to understand how two things:
- How running a computer program would allow me to create a fully functioning webpage that would take user inputs and transform the HTML accordingly.
- How to use an automated computer program to fetch information from the internet and render the fetched data on a webpage (for this I used the Beautiful Soup 4 Library).

Note: little attention has been brought to the actual style of the page, the focus was on the python code.



How does it work?

Simply run the create_simple_movie_website.py with an adapted interpreter and a webpage with my favorite movies and some information about them should automatically be created.



How do I adapt it to my taste?

Simply change the input in the create_simple_movie_website.py file in this way:

snatch = media.Movie("http://www.imdb.com/title/tt0208092/","https://www.youtube.com/watch?v=ni4tEtuTccc")

will become...

[your_movie] = media.Movie("[the_movie_imdb_url]","[the_movie_trailer_youtube_url]")

Note: only links to imdb and youtube are working with the current version. It is however possible to tweak this with a little more work.
