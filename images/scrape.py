import os
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://www.exploratorium.edu/exhibits/mutant_flies/mutant_flies.html"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = [img for img in soup.find_all('img')]
for pic in imgs:
	img_links = [each.get('src') for each in imgs]
	print img_links
	for link in img_links:
		filename = link.split('/')[-1]
		urllib.urlretrieve('http://www.exploratorium.edu/exhibits/mutant_flies/'+link, filename)