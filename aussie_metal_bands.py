'''
collect metal band names from http://www.metalunderground.com/
'''

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


base_url = "http://www.metalunderground.com/bands/country/australia/"

urls = [base_url + "page/{}/".format(p) for p in range(1,7)]

artists = []

for url in urls:
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	the_div = soup.find('div', id='content')
	if the_div:
		the_tab = the_div.find('table')
		if the_tab:
			allrows = the_tab.find_all('tr')
			if allrows:
				for row in allrows:
					the_td = row.find('td')
					if the_td:
						artist_name = the_td.text.lower().strip()
						if (len(artist_name) > 1) and ('\n'  not in artist_name):
							artists.append(artist_name)

artists = sorted(list(set(artists)))

print(f'collected {len(artists)} metal band names')

with open('aussie_metal_artists.txt','w') as f:
	for a in artists:
		f.write(f"{a}\n")