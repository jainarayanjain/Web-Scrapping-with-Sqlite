import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://en.wikipedia.org/wiki/Linkin_Park_discography"
Baseurl = "https://en.wikipedia.org"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find("table", {"class": "wikitable plainrowheaders"})
rows = table.find_all('tr')[2:]
albumname = []
for r in rows:
    albumname.append({"name": r.th.text.strip(), "link": r.find('th').a['href']})

for i in (albumname):
    url2 = urljoin(Baseurl, i['link'])

    """Code to create csv file """
    filename = i['name']
    fullpath = str(filename) + ".csv"
    """CSV file is created """

    nextpage = requests.get(url2)
    soup2 = BeautifulSoup(nextpage.content, 'html.parser')
    table2 = soup2.find("table", {"class": "tracklist"})
    rows2 = table2.find_all('tr')[1:-1]
    albumsrecord = []

    for r2 in rows2:
        rr = r2.find_all("td", {"class": "tracklist-length"})
        albumsrecord.append({"name": r2.td.text.replace('"','').replace('"',''), "length": rr[0].text})

    keys = albumsrecord[0].keys()

    with open(fullpath, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(albumsrecord)

    print(albumsrecord)