from bs4 import BeautifulSoup
import requests
import re

link = "https://www.foxsports.com/ufc/fighters?weightclass=0&teamId=0&season=2018&position=0&page=73&country=0&grouping=0&weightclass=1&association=0&circuit=0&competition=0&organizationId=0"

def get_source(link):
	return requests.get(link).text

source = get_source(link)
soup = source.BeautifulSoup('lxml')

matches = soup.find_all('a')
