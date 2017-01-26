import media  # media module contains class Movie

import fresh_tomatoes 
""" fresh_tomatoes module contains the method open_movies_page and the CSS/HTML
code to construct our movie trailer HTML page """

#  create instance for each movie using class Movie
gladiator = media.Movie("Gladiator",
	"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
	"https://www.youtube.com/watch?v=owK1qxDselE&t=12s")

prestige = media.Movie("The Prestige",
	"https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
	"https://www.youtube.com/watch?v=o4gHCmTQDVI")

django = media.Movie("Django Unchained",
	"https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
	"https://www.youtube.com/watch?v=eUdM9vrCbow")

interstellar = media.Movie("Interstellar",
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=Lm8p5rlrSkY")

braveheart = media.Movie("Braveheart",
	"https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
	"https://www.youtube.com/watch?v=wj0I8xVTV18")

# create data list with all movie instances
movies = [gladiator,prestige,django,interstellar,braveheart]

# pass movie data list to generate HTML page
fresh_tomatoes.open_movies_page(movies)



