class Movie():
	""" 
	This class provides a framework to store movie related information 

	Required input variables are (
		movie_title,
		thumbnail_link, 
		trailer_link)

	"""

	def __init__(self,movie_title,thumbnail_link,trailer_link):
		print "Movie Constructor called"
		self.title = movie_title
		self.poster_image_url = thumbnail_link
		self.trailer_youtube_url = trailer_link





