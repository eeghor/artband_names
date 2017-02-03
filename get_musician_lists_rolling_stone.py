"""

SCRAPE MUSICIAN LISTS from WIKIPEDIA

--- igor k. 03FEB2017 ---

"""

import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import string


MUS_FILE = "performer_list.txt"
START_URL = "http://www.rollingstone.com/music/artists/"
	
print("====> scraping performer names from rolling stone")

musicians = []

t0 = time.time()

for lttr in string.ascii_lowercase:

	next_page = START_URL + lttr

	print("retrieving page {}...".format(next_page), end="")	
	page = requests.get(next_page)
	
	if page.status_code == 200:
		print("ok")
	else:
		print("error {}!".format(year))

	# create a soup object
	soup = BeautifulSoup(page.content, 'html.parser')

	for some_a in soup.find_all("a", href=re.compile("artists")):
		if some_a.find("div", class_="content-card-title"):
			grabbed_musician = some_a.text.strip().lower()  # note this can be empty after stripping
			if len(grabbed_musician) > 1:
				musicians.append(some_a.text.strip().lower())


t1 = time.time()

NMUS = len(musicians)

print("found {} performer names...".format(NMUS))
print("elapsed time: {} seconds".format(round(t1-t0,1)))
print("saving performers to {}...".format(MUS_FILE), end="")
# save the obtained musicians to a file
with open(MUS_FILE, "w") as f:
	for m in musicians:
		f.write("{}\n".format(m))
print("ok")
print("all done. enjoy.")

