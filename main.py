import os
from spotify_auth import authenticate_spotify
from billboard_playlist import create_billboard_playlist
from personalized_playlist import create_personalized_playlist
from playlist_analyzer import analyze_playlist

def main():
    sp = authenticate_spotify()

    while True:
        print("\nSpotify Playlist Manager")
        print("1. Create Billboard 100 Playlist")
        print("2. Create Personalized Playlist")
        print("3. Analyze and Optimize Playlist")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            date = input("Enter the date for Billboard 100 (YYYY-MM-DD): ")
            create_billboard_playlist(sp, date)
        elif choice == '2':
            create_personalized_playlist(sp)
        elif choice == '3':
            playlist_id = input("Enter the Spotify playlist ID to analyze: ")
            analyze_playlist(sp, playlist_id)
        elif choice == '4':
            print("Thank you for using Spotify Playlist Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
























