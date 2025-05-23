import os, json
#from dotenv import load_dotenv
from requests import get, post
from dotenv import load_dotenv

# Login https://www.musixmatch.com/
headers = {
    "Content-Type": "application/json", "Accept": "application/json"
}

load_dotenv()
api_key = os.getenv("api_key")


def search_for_artist(artist_name):
    url = "https://api.musixmatch.com/ws/1.1/"
    query = f"artist.search?q_artist={artist_name}&page_size"
    query_url = url + query + api_key
    # print(query_url)
    result = get(query_url, headers=headers)
    # print(result)
    json_result = json.loads(result.content)
    # print(json_result)
    json_result = json_result['message']['body']['artist_list']

    if len(json_result) == 0:
        print("no artist with this name exist.")
        return None

    return json_result[0]

def get_album_by_artist(artist_id):
  url = "https://api.musixmatch.com/ws/1.1/artist.albums.get?"
  query = f"artist_id={artist_id}&s_release_date=desc&g_album_name"
  query_url = url + query + api_key
  # print(query_url)
  result = get(query_url, headers=headers)
  json_result = json.loads(result.content)
  json_result = json_result['message']['body']['album_list']

  return json_result

def get_songs_by_artist(album_id):
  url = "https://api.musixmatch.com/ws/1.1/album.tracks.get?"
  query = f"album_id={album_id}&page=1&page_size=26"
  query_url = url + query + api_key
  # print(query_url)
  result = get(query_url, headers=headers)
  json_result = json.loads(result.content)
  json_result = json_result['message']['body']['track_list']
  return json_result

def get_songs_by_lyrics(track_id):
  url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?"
  query = f"track_id={track_id}"
  query_url = url + query + api_key
  result = get(query_url, headers=headers)
  json_result = json.loads(result.content)
  json_result = json_result['message']['body']['lyrics']
  # print(json_result)
  return json_result

# search_artist = search_for_artist("Miley Cyrus")
# print(search_artist)
