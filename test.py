from bs4 import BeautifulSoup
import os
import re
import unicodedata

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

	
class spider(Crawler):
	def __init__(self, source, link = 'n/a', branch = ''):
		self.source = source
		self.branch = branch
		self.link = link
		self.soup = BeautifulSoup(self.source, 'html.parser')
		

files = os.listdir('./htmls/')
pages = [ open('./htmls/'+file, 'r').read() for file in files ]

crawler_obj = spider(pages[1],'https://pythonprogramming.net')
crawler_obj.start()


