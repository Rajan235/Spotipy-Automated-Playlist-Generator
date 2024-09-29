# Spotify Playlist Manager

Spotify Playlist Manager is a Python-based command-line tool that allows users to create, analyze, and optimize Spotify playlists. This project provides various features to enhance your Spotify playlist experience.

## Features

1. **Create Billboard 100 Playlist**: Generate a playlist based on the Billboard Hot 100 chart for a specific date.
2. **Create Personalized Playlist**: Build a custom playlist based on your top artists, genres, and tracks.
3. **Analyze and Optimize Playlist**: Examine an existing playlist, remove duplicates, and export playlist data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Spotify Developer account and API credentials
- Required Python libraries: `spotipy`, `beautifulsoup4`, `requests`

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/spotify-playlist-manager.git
   cd spotify-playlist-manager
   ```

2. Install the required Python libraries:

   ```
   pip install spotipy beautifulsoup4 requests
   ```

3. Set up your Spotify API credentials:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create a new application
   - Set the redirect URI to `http://example.com`
   - Note your Client ID and Client Secret

4. Update the `spotify_auth.py` file with your Spotify API credentials:
   ```python
   client_id = "your_client_id_here"
   client_secret = "your_client_secret_here"
   ```

## Usage

Run the main script to start the Spotify Playlist Manager:

```
python main.py
```

Follow the on-screen prompts to choose from the available options:

1. Create Billboard 100 Playlist
2. Create Personalized Playlist
3. Analyze and Optimize Playlist
4. Exit

### Creating a Billboard 100 Playlist

When prompted, enter a date in the format YYYY-MM-DD to create a playlist based on the Billboard Hot 100 chart for that date.

### Creating a Personalized Playlist

This option will automatically create a playlist based on your top artists, genres, and tracks on Spotify.

### Analyzing and Optimizing a Playlist

Enter the Spotify playlist ID when prompted. The tool will provide analysis results and offer options to remove duplicates and export playlist data.

## Contributing

Contributions to the Spotify Playlist Manager are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Spotipy](https://spotipy.readthedocs.io/) for the Spotify Web API wrapper
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for web scraping capabilities
- [Billboard.com](https://www.billboard.com/) for chart data
