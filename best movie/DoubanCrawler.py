"""
url example:
  https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国
"""

"""
return a string corresponding to the URL of douban movie lists given category and location.
@param category: str
@param location: str
"""
def getMovieUrl(category, location)
	url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
	return ','.join([category, location])

