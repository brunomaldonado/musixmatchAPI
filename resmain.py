# from dotenv import load_dotenv
from requests import post, get
import os
import json
import re
import json
import server

headers = {'Content-Type': "application/json", 'Accept': "application/json"}

# http://api.musixmatch.com/ws/1.1/çapikey=5f423b7772a80f77438407c8b78ff305&format=json&domain=www.mylyricswebsite.com

# format_url = "?format=json&callback=callback"
# base_url = "https://api.musixmatch.com/ws/1.1/"
# "&q_artist="
# artist.search?q_artist=prodigy&page_size=5
# format_url = "?format=json&callback=callback"

# artist.search?q_artist=prodigy&page_size=5
# track.get?commontrack_id=5920049


# load_dotenv()
# api_key = os.getenv("api_key")
api_key = "&apikey=d29b01a27dd289021382091564155a98"
# print(api_key)

def search_for_artist(artist_name):
  url = "https://api.musixmatch.com/ws/1.1/artist.search?"
  query = f"q_artist={artist_name}&page_size=1?format=json&callback=callback"

  query_url = url + query + api_key

  # print(query_url)
  # request = requests.get(query_url, headers=headers)
  # data = request.json()
  # data = data['message']['body']
  # print(data)
  # print(json.dumps(data, sort_keys=True, indent=2))
  # json_result = json.dumps(data, sort_keys=True, indent=2)
  # print(json_result)
  # if len(json_result) == 0:
  #   print("no artist with this name exist...")
  #   return None
#   return json_result[0]

  result = get(query_url, headers=headers)
  json_result = json.loads(result.content)
  json_result = json_result['message']['body']['artist_list']
# print(len(json_result))
# print("json results --------------------- ", json_result)
# print(json_result[3]['artist']['artist_name'])

  if len(json_result) == 0:
    print("no artist with this name exist...")
    return None
  return json_result[0]


def get_albums_by_artist(artist_id):
  url = "https://api.musixmatch.com/ws/1.1/artist.albums.get?"
  query = f"artist_id={artist_id}&s_release_date=desc&g_album_name=1"
  query_url = url + query + api_key
  # print(query_url)
  result = get(query_url, headers=headers)
  json_result = json.loads(result.content)
  json_result = json_result['message']['body']['album_list']
  # print("len album", len(json_result))
  # print("name album", json_result[0])

  # data_list = json_result
  # print("album list", data_list)

  # for index, album in enumerate(data_list):
  #   # print("index", index, album)
  #   print(f"{index + 1}. {album['album']['album_name']}")

  # print("album name", json_result[1]['album']['album_name'])
  # print("album name", json_result[2]['album']['album_name'])
  # print("album name", json_result[3]['album']['album_name'])
  # print("album name", json_result[4]['album']['album_name'])
  # print("album name", json_result[5]['album']['album_name'])
  # print("album name", json_result[6]['album']['album_name'])

  # print(json_result[2]['album']['album_name'], json_result[2]['album']['artist_name'])
  # print(json_result[2]['album']['album_name'])

  # if len(data_list) == 0:
  #   print("no album exist...")
  #   return None
  # return data_list[0]
  return json_result


def get_songs_by_artist(album_id):
  url = "https://api.musixmatch.com/ws/1.1/album.tracks.get?"
  query = f"album_id={album_id}&page=1&page_size=26"
  # url = "https://api.musixmatch.com/ws/1.1/track.search?"
  # query = f"q_artist={artist_name}&page_size=10&page=3&s_track_rating=desc"
  query_url = url + query + api_key
  # print(query_url)
  result = get(query_url, headers=headers)
  json_result = json.loads(result.content)
  json_result = json_result['message']['body']['track_list']
  # print(json_result)
  return json_result


# artist_search = search_for_artist("Miley Cyrus")
# print(artist_search)
# print("\n   Artist name: ", artist_search['artist']["artist_name"])
# artist_id = artist_search['artist']['artist_id']
# artist_albums = get_albums_by_artist(artist_id)
# # print(f"album: ", artist_albums)
# print(f"\nalbum id: ", artist_albums[0]['album']['album_id'])
# album_id = artist_albums[1]['album']['album_id']
# # print("album id", album_id)
# # print(f"artist name: ", artist_albums['album']['artist_name'])
# # print(f"album copyright: ", artist_albums['album']['album_copyright'])
# # print(f"album release date: ", artist_albums['album']['album_release_date'])
# # print(f"album label: ", artist_albums['album']['album_label'])
# # print(f"album rating:", artist_albums['album']['album_rating'])
# # print(f"album id:", artist_albums['album']['album_id'])
# print("\nAlbums.\n")

# for idx, album in enumerate(artist_albums):
#     print(f"{idx + 1}. {album['album']['album_name']}")
#     # print(f"{idx + 1}. {album['album']['album_id']}")
#     # album_id.append(album['album']['album_id'])
# print()

# album_tracks = get_songs_by_artist(album_id)
# str_date = album_tracks[0]['track']['updated_time']
# print("   Album name:", album_tracks[0]['track']['album_name'])
# print("   Artist:", album_tracks[0]['track']['artist_name'])
# print("   Date:", int(re.search(r'\d+', str_date)[0]))
# # int(re.search(r'\d+', str_date)[0])
# # print(int(re.search(r'\d+', str_date)[0]))
# print("\nTracks.\n")
# # print(album_tracks)

# for idx, track in enumerate(album_tracks):
#     print(f"{idx + 1}. {track['track']['track_name']}")

def print_options():
  print("\n\n")
  options = [
    "[1] add songs",
    "[2] select album",
    "[3] search artist",
    "[4] favourites",
    "[5] exit"
  ]

  for i in range(0, len(options), 3):
    print("{:<15} {:<15} {:<15}".format(
      *options[i:i+3], *[''] * (3 - len(options[i:i+3]))
    ))

def main():
  print("\n")
  print("-" * 50)
  search = input(f"Enter Artist name: ")
  artist_search = search_for_artist(search)
  # print(artist_search)
  # print("-" * 50)
  # print("         Artist:", artist_search['artist']["artist_name"])
  # print("         Country:", artist_search['artist']["artist_country"])
  # print("-" * 50)
  artist_id = artist_search['artist']['artist_id']
  # print(artist_id)
  artist_album = get_albums_by_artist(artist_id)
  # print(artist_album)

  if len(artist_album) == 0:
    main()
  else:
    pass
  
  print("-" * 50)
  print(f"          Artist: {artist_search['artist']["artist_name"]}, {
        artist_search['artist']["artist_country"]}")
  print(f"          {len(artist_album)} Album")
  print("-" * 50)
  for idx, album in enumerate(artist_album):
    print(f"{idx + 1} {album['album']['album_name']}")

  album_id = [album['album']['album_id'] for album in artist_album]
  # print(album_id)
  # print(album_id[0])

  def select_index(selection):
    if 1 <= selection <= len(album_id):
      return selection - 1
    else:
      return "Invalid selection"
  print()
  selection = int(input(f"Select # album to play: "))
  # print(select_album)
  print()

  list_songs = []
  favourite_songs = []
  def print_tracks():
    # print(list_songs)
    unique_songs = set(list_songs)
    for idx, songs in enumerate(unique_songs):
        print(f"{idx + 1} {songs}")
    print()
    def select_index(selection):
      if 1 <= selection <= len(list_songs):
        return selection - 1
      else:
        return "Invalid Selection"
      
    selection = int(input("\nSelect # song to add: "))
    add_song = select_index(selection)
    favourite_songs.append(list_songs[add_song])
    while True:
      option = int(input("\n1.- Continue    2.- Exit\nOption: "))
      if option == 1:
        selection = int(input("\nSelect # song to add: "))
        add_song = select_index(selection)
        favourite_songs.append(list_songs[add_song])
      elif option == 2:
        break
      
  def album_track():
    select_album = select_index(selection)
    album_songs = get_songs_by_artist(album_id[select_album])
    # print(album_songs)
    print("-" * 50)
    print(f"         Album: {
        artist_album[select_album]['album']["album_name"]}")
    print(f"         Artist: {
        artist_album[select_album]['album']["artist_name"]}")
    print(f"         Date: {
        artist_album[select_album]['album']["album_release_date"]}")
    print(f"         Copyright: {
        artist_album[select_album]['album']["album_copyright"]}")
    print(f"         {len(album_songs)} Tracks")
    print("-" * 50)
    for idx, track in enumerate(album_songs):
        print(f"{idx + 1} {track['track']['track_name']}")
        list_songs.append(track['track']['track_name'])
  album_track()
  
  while True:
    print_options()
    option = int(input("\nOption: "))
    if option == 1:
      print("\nAdd songs as favorites\n")
    #   print(list_songs)
      print_tracks()
    elif option == 2:
      print("-" * 50)
      print(f"          Artist: {artist_search['artist']["artist_name"]}")
      print(f"          Country: {artist_search['artist']["artist_country"]}")
      print(f"          {len(artist_album)} Album")
      print("-" * 50)
      for idx, album in enumerate(artist_album):
        print(f"{idx + 1} {album['album']['album_name']}")
      print()
      selection = int(input(f"\nSelect # album to play: "))
      album_track()
    #   return
    elif option == 3:
      main()
    elif option == 4:
      print("-" * 50)
      print("          ⭐️ Favourite Songs")
      print(f"          Artist: {artist_search['artist']["artist_name"]}")
      print(f"          Country: {artist_search['artist']["artist_country"]}")
      print("-" * 50)
      unique_favourites = set(favourite_songs)
      for idx, fav in enumerate(unique_favourites):
        print(f"{idx + 1} {fav}")
      print()
      if len(favourite_songs) == 0:
        print("No songs added as favorites")
      else:
        pass
    elif option == 5:
      return
  
#   while True:
#     retry = input(f"\n\nDo yu want to run again? (y/n): ").strip().lower()
#     if retry == 'y':
#       main()
#       return
#     elif retry == 'n':
#       return
#     else:
#       print(f"Please enter 'y' or 'n'")


if __name__ == '__main__':
    main()
