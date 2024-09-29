from bs4 import BeautifulSoup
import requests

def create_billboard_playlist(sp, date):
    user_id = sp.me()["id"]
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    soup = BeautifulSoup(response.text, 'html.parser')
    songs = soup.find_all("li", {"class": "o-chart-results-list__item"})

    song_data = []
    for song in songs:
        title_element = song.find("h3", id="title-of-a-story")
        artist_element = song.find("span", {"class": "c-label"})
        if title_element and artist_element:
            title = title_element.get_text(strip=True)
            artist = artist_element.get_text(strip=True)
            song_data.append((title, artist))

    year = date.split("-")[0]
    spotify_song_uris = []

    for title, artist in song_data:
        result = sp.search(q=f"track:{title} artist:{artist} year:{year}", type="track", limit=1)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            spotify_song_uris.append(uri)
        except IndexError:
            print(f"{title} by {artist} doesn't exist on Spotify. Skipped.")

    playlist_name = f"{date} Billboard 100"
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description="Live your time")

    playlist_id = playlist["id"]
    if spotify_song_uris:
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=spotify_song_uris)

    print(f"Playlist '{playlist_name}' created successfully with {len(spotify_song_uris)} tracks.")

