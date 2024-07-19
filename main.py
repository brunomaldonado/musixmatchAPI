# from dotenv import load_dotenv
from requests import post, get
import os
import json
import re
import json
from utils import server
from utils.mediaPlayer import Track, MediaPlayerQueue, print_intro
from random import randint
import time

# headers = {'Content-Type': "application/json", 'Accept': "application/json"}

def print_options():
  print("\n\n")
  options = [
    "[1] Ądd Ş🎧ngs",
    "[2] Şelect Ąlbum",
    "[3] Șearch 🎭",
    "[4] ⚝ Favourites",
    "[5] Ș🥁ng l¥rįç$",
    "[6] Ęxit..."
  ]

  for i in range(0, len(options), 3):
    print("{:<15} {:<15} {:<15}".format(
      *options[i:i+3], *[''] * (3 - len(options[i:i+3]))
    ))
    
def indentation_title1(title, width=46, char_delay=0):
  # print(" " * 1, "-" * 53)
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 9
  initial_spacing = " " * 2

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "
    
  title_lines.append(current_line.strip())
#   print(title_lines)
  # print(initial_spacing, end="", flush=True)
  # print(end="", flush=True)
  formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      formatted_title += line
      # for char in line:
      #   print(char, end="", flush=True)
      #   time.sleep(char_delay)
    else:
      formatted_title += "\n" + spacing_line + line[len(empty_line):]
      # print("\n", spacing_line, end="", flush=True)
      # for char in line[len(empty_line):]:
      #   print(char, end="", flush=True)
      #   time.sleep(char_delay)    
  
  return formatted_title

def indentation_title2(title, width=46, char_delay=0):
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 13
  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "
  title_lines.append(current_line.strip())
  formatted_title = ""
  for i, line in enumerate(title_lines):
    if i == 0:
      formatted_title += line
    else:
      formatted_title += "\n" + spacing_line + line[len(empty_line):]
  return formatted_title

def main():
  media = MediaPlayerQueue()
  # print("\n")
  # print("" * 1, "-" * 53)
  print("-" * 50)
  search = input(f"Enter Artist name: ")
  artist_search = server.search_for_artist(search)
  artist_id = artist_search['artist']['artist_id']
  # print(artist_id)
  artist_album = server.get_album_by_artist(artist_id)
  # print(artist_album)

  if len(artist_album) == 0:
    main()
  else:
    pass
  
  print("-" * 50)
  print(f"  Artist: {artist_search['artist']['artist_name']}")
  print(f"  Country: {artist_search['artist']['artist_country']}")
  print(f"  {len(artist_album)} Album")
  print("-" * 50)

  album_name = []
  for idx, album in enumerate(artist_album, start=1):
    # print(f"{idx:2} {album['album']['album_name']}")
    albums = album['album']['album_name']
    album_name.append(albums)

  for idx, album in enumerate(album_name, start=1):
    count = idx + 1
    track = f"track{count}"
    track = Track(album)
    media.add_track(track)
  
  # media.pause()
  media.delay()
  print()

  songs_list = []
  favourite_songs = []
  def tracklist():
    # print(songs_list)
    for song in songs_list:
      # check if the count of song is > 1 (repeating item)
      if songs_list.count(song) > 1:
      # if True, remove the first occurrence of song
          songs_list.remove(song)
    # print(f"{songs_list} {len(songs_list)}")
    # for idx, songs in enumerate(songs_list, start=1):
    #     print(f"{idx:2} {songs}")
            
    for idx, song in enumerate(songs_list, start=1):
      count = idx + 1
      track = f"track{count}"
      track = Track(song)
      media.add_track(track)
    
    media.delay()
    print()
    
    def select_index(selection):
      if 1 <= selection <= len(songs_list):
        return selection - 1
      else:
        return "Invalid Selection"
    
    print()

    while True:
      selection = int(input("\nSelect # song to add: "))
      add_song = select_index(selection)
    #   option = int(input("\n[1] Select # Song   [2] Exit\nOption: "))
      if isinstance(add_song, int):
        favourite_songs.append(songs_list[add_song])
        # selection = int(input("\nSelect # song to add: "))
        # add_song = select_index(selection)
        # favourite_songs.append(songs_list[add_song])
      else:
        print("invalid selection")
      option = int(input("\n[1] Select # Song   [2] Exit\nOption: "))
      if option == 2:
        break

  album_tracks_data = []
  def album_list():
    album_id = [album['album']['album_id'] for album in artist_album]

    def select_index(selection):
      if 1 <= selection <= len(album_id):
        return selection - 1
      else:
        return "Invalid selection"
    print()
    selection = int(input(f"\nSelect # album: "))
    # print(select_album)
    select_album = select_index(selection)
    album_songs = server.get_songs_by_artist(album_id[select_album])
    album_tracks_data.append(album_songs)
    # print(album_songs)

    # print("" * 1, "-" * 53)
 
    print("-" * 50)
    # print(f"  Album: {artist_album[select_album]['album']['album_name']}")
    print(f"  Album: {indentation_title1(artist_album[select_album]['album']['album_name'])}")
    print(f"  Artist: {artist_album[select_album]['album']['artist_name']}")
    print(f"  Date: {artist_album[select_album]['album']['album_release_date']}")
    print(f"  Copyright: {indentation_title2(artist_album[select_album]['album']['album_copyright'])}")
    print(f"  {len(album_songs)} Tracks")
    print("-" * 50)

    album_tracks = [] # for the delay function from mediaPlayer 
    for idx, track in enumerate(album_songs, start=1):
        # print(f"{idx:2} {track['track']['track_name']}")
        album_tracks.append(track['track']['track_name'])
        songs_list.append(track['track']['track_name'])
    
    for idx, name in enumerate(album_tracks, start=1):
      count = idx + 1
      track = f"track{count}"
      track = Track(name)
      media.add_track(track)
    
    media.delay()
    print()
  album_list()

  def song_lyrics():
    print()
    print("-" * 50)
    # print("Songs L🎷R₷¥℞₡₵𝖎 Ŀ")
    # print("Songs L🎷R₷¥℞₡₵  𝖎Ŀ")
    # print("Songs Ŀ¥℞ŞⱾɨ₵₷")
    print(" Songs Ŀ¥℞ɨℂ$")
    # print("Songs Ŀ¥℞𝖎ℂ$")
    # print("Songs L🎷R₷¥℞₡₵  𝖘§ℭ𝕮ℂĿ¥℞𝖎₵₷")
    print("-" * 50)
    # print(album_tracks_data)
    
    # for idx, song in enumerate(songs_list):
    #   # print(song)
    #   count = idx + 1
    #   track = f"track{count}"
    #   track = Track(song)
    #   media.add_track(track)
    # media.delay()

    id_songs = [id['track']['track_id'] for sublist in album_tracks_data for id in sublist]
    # print("\n")
    # print(id_songs)
    name_songs = [name['track']['track_name'] for sublist in album_tracks_data for name in sublist]
    # id_map = {index: id_value for index, id_value in enumerate(id_songs)}
    # print(id_map)
    # name_map = {name: track for name, track in enumerate(name_songs)}
    # print(name_map)
    # print()
    # print("name songs", name_songs)
    # print()
    seen = set()
    single_names = []
    unique_id = []

    for id in id_songs:
      if id not in seen:
        seen.add(id)
        unique_id.append(id)
      else:
        if unique_id.count(id) < 1:
          unique_id.append(id)
    # print()
    # print(unique_id)
    # print()
    id_map = {index: id_value for index, id_value in enumerate(unique_id)}

    for name in name_songs:
      if name not in seen:
        seen.add(name)
        single_names.append(name)
      else:
        if single_names.count(name) < 1:
          single_names.append(name)
    # print()
    # print(single_names)
    # print() 
    name_map = {name: track_name for name, track_name in enumerate(single_names)}

    for idx, name in enumerate(single_names, start=1):
      # print(f"{idx:2} {name}")
      count = idx + 1
      track = f"track{count}"
      track = Track(name)
      media.add_track(track)
    media.delay()

    def select_index(selection):
      if 1 <= selection <= len(unique_id):
        return selection - 1
      else:
        return "Invalid selection"
    print()
    while True:
      select_track = int(input("\nGet lyrics # track: "))
      track = select_index(select_track)
      # track_id = id_map[track]
      # track_name = name_map[track]
      # lyrics_songs =  server.get_songs_by_lyrics(track_id)
      # print("\n")
      # print(f"Title: {track_name}")
      # print("\n" + lyrics_songs['lyrics_body'])
      if isinstance(track, int):
        track_id = id_map[track]
        track_name = name_map[track]
        lyrics_songs =  server.get_songs_by_lyrics(track_id)
        print("\n")
        print(f"Title: {track_name}")
        print("\n" + lyrics_songs['lyrics_body'])
        # print()
        # print(lyrics_songs)
      else:
        print("invalid selection")
      option = int(input("\n[1] Select other # track?   [2] Exit\nOption: "))
      if option == 2:
        break


  while True:
    print_options()
    option = int(input("\nOption: "))
    if option == 1:
      print()
      print("-" * 50)
      print("  Add songs as favorites")
      print("-" * 50)
    #   print(songs_list)
      tracklist()
    elif option == 2:
      print("-" * 50)
      print(f"  Artist: {artist_search['artist']['artist_name']}")
      print(f"  Country: {artist_search['artist']['artist_country']}")
      print(f"  {len(artist_album)} Album")
      print("-" * 50)
      
      for idx, album in enumerate(album_name, start=1):
        count = idx + 1
        track = f"track{count}"
        track = Track(album)
        media.add_track(track)
    
      media.delay()
      album_list()
    #   return
    elif option == 3:
      main()
    elif option == 4:
      print("-" * 50)
      print(" ⭐️ Favourite Songs")
      print(f"  Artist: {artist_search['artist']['artist_name']}")
      print(f"  Country: {artist_search['artist']['artist_country']}")
      print("-" * 50)
      print()
      if len(favourite_songs) == 0:
        print("No songs added as favorites")
      else:
        print_intro(" Playing Songs")
        # print(favourite_songs)
        seen = set()
        result = []
        for item in favourite_songs:
          if item not in seen:
            seen.add(item)
            result.append(item)
          else:
            if result.count(item) < 1:
              result.append(item)
        # print(result)
        print("\n")
        # print("Track")
        for idx, song in enumerate(result):
        #   print(f"{idx + 1} {song}")
          count = idx + 1
          track = f"track{count}"
          track = Track(song)
          media.add_track(track)
        media.play()
    elif option == 5:
      song_lyrics()
    elif option == 6:
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