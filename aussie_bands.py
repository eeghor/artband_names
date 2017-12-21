'''
get artist names from http://www.aussiebands.com.au/
'''

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

urls = ["http://www.aussiebands.com.au/australian_kids_music.htm", "http://www.aussiebands.com.au/australian_rock_and_pop_artists.htm",
"http://www.aussiebands.com.au/australian_indie_and_hip_hop_artists.htm", "http://www.aussiebands.com.au/australian_tribute_bands_and_singers.htm",
"http://www.aussiebands.com.au/australian_country_artists.htm", "http://www.aussiebands.com.au/australian_blues_artists.htm",
"http://www.aussiebands.com.au/australian_jazz_artist.htm",
]

artists = []

for url in urls:
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	all_ps = soup.find_all('p')
	if all_ps:
		for p in all_ps:
			if p.find('a'):
				artists.append(' '.join([unidecode(w) for w in p.find('a').text.lower().replace('\n',' ').split()]))

artists = sorted(list(set(artists)))

with open('aussie_artists.txt','w') as f:
	for a in artists:
		f.write(f"{a}\n")
