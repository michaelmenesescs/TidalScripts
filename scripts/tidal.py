from bs4 import BeautifulSoup
import pandas as pd

with open('page.html') as page:
    soup = BeautifulSoup(page, 'html.parser')


tracks = []

rows = soup.findAll('div', attrs={'class', 'tableRow--b7mNR'})

for row in rows:
    #Artist Names
    a = row.find('a', attrs = {'class', 'css-r22orw'})
    artist_name = a['title']

    #Song Names
    s = row.find('span', attrs = {'class', 'titleText--1LuE_ table--inactive-title'})
    song_name = s['title']

    #Album Names
    alb = row.find('a', attrs = {'class', 'albumText--1OiK4 css-r22orw'})
    album_name = alb['title']

    #Tidal Artist ID
    artist_id = a['href']

    #Tidal Song ID
    song_id = s['data-id']

    #Tidal Album ID
    album_id = alb['href']

    song_info = (artist_name, song_name, album_name, artist_id, song_id, album_id)

    tracks.append(song_info)
    #print(song_info)



songs = pd.DataFrame(tracks, columns=['Artist', 'Song', 'Album', 'Artist ID', 'Song_ID', 'Album_ID'])

songs.to_csv('./songs.csv')
print(songs)