
def create_personalized_playlist(sp):
    user_id = sp.me()["id"]
# get user top artist
    top_artists_data = sp.current_user_top_artists(limit=3)
    top_artists = [artist['id'] for artist in top_artists_data['items']]

    # Fetch tracks for top 3 artists (20 tracks total, ~6-7 per artist)
    artist_tracks = []
    for artist_id in top_artists:
        artist_top_tracks = sp.artist_top_tracks(artist_id)['tracks']
        for track in artist_top_tracks[:7]:  # limit to 6-7 songs per artist
            if len(artist_tracks) < 20:
                artist_tracks.append(track['uri'])

    # Extract the genres from top artists
    top_genres = []
    for artist in top_artists_data['items']:
        top_genres.extend(artist['genres'])

    # Get the top 5 unique genres
    top_genres = list(set(top_genres))[:5]

    # Fetch 15 songs from these genres (3 songs per genre)
    genre_tracks = []
    for genre in top_genres:
        result = sp.search(q=f'genre:{genre}', type='track', limit=3)
        for track in result['tracks']['items']:
            if len(genre_tracks) < 15:
                genre_tracks.append(track['uri'])

    print(f"Collected {len(genre_tracks)} tracks from top genres.")

    # Get user's top played tracks (limit 15)
    top_tracks_data = sp.current_user_top_tracks(limit=15)
    top_tracks = [track['uri'] for track in top_tracks_data['items']]

    print(f"Collected {len(top_tracks)} tracks from user's top played songs.")

    # Combine all tracks (up to 50 songs)
    total_tracks = artist_tracks + genre_tracks + top_tracks

    # Ensure a max of 50 tracks
    total_tracks = total_tracks[:50]

    # Create a new playlist for the user
    playlist_name = "Top Artists, Genres, and Tracks Playlist"
    playlist_description = "A playlist generated from your top artists, genres, and played songs."
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

    # Add tracks to the new playlist
    playlist_id = playlist['id']
    if total_tracks:
        sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=total_tracks)

    print(f"Playlist '{playlist_name}' created successfully with {len(total_tracks)} tracks.")