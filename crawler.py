from bs4 import BeautifulSoup
import requests
import re

link = "http://www.imdb.com/"
link2 = "http://www.imdb.com/title/tt0944947/?ref_=nm_knf_i1"
visited = []
to_go = [link2]

def get_source(link):
	return requests.get(link).text

def get_links(source):
	""" returns all the links found on this page """
	""" im thinking something with args* and more generic """

	soup = BeautifulSoup(source, "lxml")
	matches = soup.find_all('a')
	good_list = ["name", "title"]

	def good_link(link):
		for item in good_list:
			if "/" + item + "/" in link:
				return 1
		return 0

	def build_link(link):
		pattern = re.compile(r'((title|name)/(nm|tt)\d*)')
		match = pattern.findall(link)
		return "http://www.imdb.com/" + match[0][0] + "/"

	def link_builder(link):
		"""" might wanna rethink that """
		matches = link.find('/')
		return matches

	matches = [ match.get('href') for match in matches if match.get('href') is not None ]
	matches = [ link for link in matches if good_link(link) ]
	matches = [ build_link(link) for link in matches ]

	return matches

"""
while len(to_go)>0:
	
	if to_go[0] not in visited:
		visited.append(to_go[0])
		to_go = to_go + get_links(get_source(to_go[0]))

	to_go = list(set(to_go))
	print ("len of to_go: ", len(to_go))
	print ("len of visited: ", len(visited))
	print (to_go[0])
	del to_go[0]

"""


class Crawler():

	def __init__(self, link, branch = ''):

		self.link = link
		self.branch = branch
		self.source = requests.get(self.dressed_link)
		self.soup = BeautifulSoup(self.source, 'lxml')
		
		pattern = re.compile(r'[a-vx-zA-Z_0-9]+\.[a-zA-Z_]+')
		match = pattern.findall(self.link)

	@property	
	def site_name(self):
		
		pattern = re.compile(r'[a-vx-zA-Z_0-9]+\.[a-zA-Z_]+')
		match = pattern.findall(self.link)
		
		striped_site_name = ''
		
		if match == []:
			raise AssertionError('Your link has an odd form.')
		else:
			striped_site_name = match[0]
		
		return striped_site_name

	def start(self):

		matches = self.soup.find_all('a')
		matches = [match.get('href') for match in matches if match.get('href') is not None]
		
		for match in matches:
			print (match)
		print (len(matches))
		
		matches = [match.encode('ascii','replace') for match in matches]                          #tosee...
		matches = [self.build_link(match) for match in matches if self.good_link(match)]

		for match in matches:
			print (match)
		print (len(matches))
	

	def good_link(self, _link):
		
		pattern = re.compile(r'[a-vx-zA-Z_0-9]+\.[a-zA-Z_]+')
		match = pattern.findall(_link)
		if match == []:
			return 1
		elif match[0] == self.site_name:
			return 1
		else:
			return 0
	
	def build_link(self,_link):
		
		if self.site_name in _link:
			index = str.find(_link, self.site_name)
			index += len(self.site_name)
			striped_link = _link[index:]
		else:
			index = _link.find('/')
			striped_link = _link[index:]
			
		return striped_link

	def dressed_link(self):

		if self.branch != '':
			return self.link + '/' + self.branch
		return self.link

links = []

links.append('https://www.foxsports.com')
links.append('https://pythonprogramming.net')
links.append('https://www.youtube.com')

spidey = Crawler(links[0],'ufc')
spidey.start()











