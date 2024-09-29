from collections import Counter
import csv
import json

def get_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def find_duplicates(tracks):
    seen = set()
    duplicates = []
    for item in tracks:
        track = item['track']
        track_id = track['id']
        if track_id in seen:
            duplicates.append(item)
        else:
            seen.add(track_id)
    return duplicates

def remove_duplicates(sp, playlist_id, duplicates):
    track_ids = [item['track']['id'] for item in duplicates]
    if track_ids:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, track_ids)
        print(f"Removed {len(track_ids)} duplicate tracks")

def calculate_playlist_duration(tracks):
    total_duration = sum([track['track']['duration_ms'] for track in tracks])
    avg_duration = total_duration / len(tracks) if tracks else 0
    total_duration_min = total_duration // 60000
    avg_duration_sec = avg_duration / 1000
    return total_duration_min, avg_duration_sec

def get_most_common_artists(tracks):
    artists = [track['track']['artists'][0]['name'] for track in tracks]
    return Counter(artists).most_common(1)[0] if artists else None

def get_most_common_genres(sp, tracks):
    genres = []
    for track in tracks:
        artist_id = track['track']['artists'][0]['id']
        artist_info = sp.artist(artist_id)
        genres.extend(artist_info['genres'])
    return Counter(genres).most_common(1)[0] if genres else None

def export_to_csv(tracks, filename="playlist_data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Track Name", "Artist", "Duration (ms)", "Album"])
        for track in tracks:
            writer.writerow([
                track['track']['name'],
                track['track']['artists'][0]['name'],
                track['track']['duration_ms'],
                track['track']['album']['name']
            ])
    print(f"Playlist data exported to {filename}")

def export_to_json(tracks, filename="playlist_data.json"):
    playlist_data = []
    for track in tracks:
        playlist_data.append({
            "track_name": track['track']['name'],
            "artist": track['track']['artists'][0]['name'],
            "duration_ms": track['track']['duration_ms'],
            "album": track['track']['album']['name']
        })
    with open(filename, 'w') as file:
        json.dump(playlist_data, file, indent=4)
    print(f"Playlist data exported to {filename}")

def analyze_playlist(sp, playlist_id):
    tracks = get_playlist_tracks(sp, playlist_id)
    duplicates = find_duplicates(tracks)
    
    print(f"\nPlaylist Analysis for ID: {playlist_id}")
    print(f"Total tracks: {len(tracks)}")
    print(f"Duplicate tracks: {len(duplicates)}")

    total_duration, avg_duration = calculate_playlist_duration(tracks)
    print(f"Total Playlist Duration: {total_duration} minutes")
    print(f"Average Track Duration: {avg_duration:.2f} seconds")

    most_common_artist = get_most_common_artists(tracks)
    most_common_genre = get_most_common_genres(sp, tracks)

    if most_common_artist:
        print(f"Most Common Artist: {most_common_artist[0]} with {most_common_artist[1]} tracks")
    if most_common_genre:
        print(f"Most Common Genre: {most_common_genre[0]} with {most_common_genre[1]} occurrences")

    if duplicates:
        choice = input("Would you like to remove duplicates? (yes/no): ").strip().lower()
        if choice == 'yes':
            remove_duplicates(sp, playlist_id, duplicates)

    export_choice = input("Would you like to export playlist data? (csv/json/no): ").strip().lower()
    if export_choice == 'csv':
        export_to_csv(tracks)
    elif export_choice == 'json':
        export_to_json(tracks)