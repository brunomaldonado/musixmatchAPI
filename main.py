from utils import server
from utils.mediaPlayer import Track, MediaPlayerQueue, print_intro
from utils.config import content_data, list_favorite_songs, list_favorite_artists, list_artists_countries, indentation_title1, indentation_title2, indentation_title3

def print_options():
  print("\n")
  options = [
    "  [1] Ⱥdd Ş🎧ngs",
    "  [2] Şelect Ⱥlbum",
    "  [3] Șearch 🎭",
    "  [4] ⚝ Favourites",
    "  [5] Ș🥁ng l¥rįç$",
    "  [6] Ęxit..."
  ]

  for i in range(0, len(options), 3):
    print("{:<15} {:<15} {:<15}".format(
      *options[i:i+3], *[''] * (3 - len(options[i:i+3]))
    ))

def main():
  media = MediaPlayerQueue()
  # print("\n")
  print("" * 1, "-" * 53)
  search = input(f" Enter Artist name: ")
  search_artist = server.search_for_artist(search)
  artist_id = search_artist['artist']['artist_id']
  # print(artist_id)
  artist_album = server.get_album_by_artist(artist_id)
  # print(artist_album)

  if len(artist_album) == 0:
    main()
  else:
    pass
  
  print("" * 1, "-" * 53)
  print(f"  Artist: {search_artist['artist']['artist_name']}")
  print(f"  Country: {search_artist['artist']['artist_country']}")
  print(f"  {len(artist_album)} Album")
  print("" * 1, "-" * 53)

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
        return " Invalid Selection"
    
    print()
    content_data.append(songs_list)
    
    attempts = 1
    while True:
      try:
        selection = int(input("\n Selected song # for add: "))
        add_song = select_index(selection)
        if isinstance(add_song, int):
          list_favorite_songs.append(songs_list[add_song])
          list_favorite_artists.append(search_artist['artist']['artist_name'])
          country = search_artist['artist']['artist_country']

          if not str(country).strip():
            artist_country = f"&$"
          else:
            artist_country = country
          list_artists_countries.append(artist_country)
        else:
          print(" Invalid selection.")
          if attempts > 3:
            tracklist()
            break
        option = int(input("\n [1] Selected song #   [2] Exit\n Option: "))
        if option == 2:
          break
      except ValueError:
        print(" Invalid selection")
      attempts += 1

  album_tracks_data = []
  def album_list():
    album_id = [album['album']['album_id'] for album in artist_album]

    def select_index(selection):
      if 1 <= selection <= len(album_id):
        return selection - 1
      else:
        return " Invalid selection"
    print()

    while True:
      try: 
        selection = int(input(f"\n Selected album #: "))
        # print(select_album)
        select_album = select_index(selection)
        if isinstance(select_album, int):
          album_songs = server.get_songs_by_artist(album_id[select_album])
          album_tracks_data.append(album_songs)
          # print(album_songs)
          # print("" * 1, "-" * 53)
          print("" * 1, "-" * 53)
          # print(f"  Album: {artist_album[select_album]['album']['album_name']}")
          print(f"  Album: {indentation_title1(artist_album[select_album]['album']['album_name'])}")
          print(f"  Artist: {artist_album[select_album]['album']['artist_name']}")
          print(f"  Date: {artist_album[select_album]['album']['album_release_date']}")
          print(f"  Copyright: {indentation_title2(artist_album[select_album]['album']['album_copyright'])}")
          print(f"  {len(album_songs)} Tracks")
          print("" * 1, "-" * 53)

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
          break
        else:
          print(" Please enter a number of lbums")
      except ValueError:
        print(" Invalid Selection!. Please enter a number")
  
  album_list()

  def favorite_sogns():
    unique_artists = []
    unique_countries = []
    for artist in list_favorite_artists:
      if artist not in unique_artists:
        unique_artists.append(artist)
    
    for country in list_artists_countries:
      if country not in unique_countries:
        unique_countries.append(country)

    artists = ', '.join(list(unique_artists))
    countries = ', '.join(list(unique_countries))

    name_artist = ['Simple Plan', 'Miley Cyrus', 'Green Day', 'Dua Lipa']
    name_artists = ', '.join(list(name_artist))

    if len(list_favorite_songs) == 0:
      print("" * 1, "-" * 53)
      print("  ⭐️ Favourite Songs")
      print("" * 1, "-" * 53)
      print()

      print("             Ɲo Ş🎧ngs Ⱥdded Ⱥs Favorites")
      print("\n")
    else:
      print("" * 1, "-" * 53)
      print("  ⭐️ Favourite Songs")
      print(f"  Artists: {indentation_title3(artists)}")
      print(f"  Artists: {indentation_title3(name_artists)}")
      print(f"  Countries: {countries}")
      print("" * 1, "-" * 53)

      seen = set()
      result = []
      for item in list_favorite_songs:
        if item not in seen:
          seen.add(item)
          result.append(item)
        else:
          if result.count(item) < 1:
            result.append(item)
      # print(result)
      print("\n")
      for idx, song in enumerate(result):
      #   print(f"{idx + 1} {song}")
        count = idx + 1
        track = f"track{count}"
        track = Track(song)
        media.add_track(track)
      media.play()

  def song_lyrics():
    print()
    print("" * 1, "-" * 53)
    print("  Şongs ƪ¥℞ɨÇ$")
    print("" * 1, "-" * 53)
    id_songs = [id['track']['track_id'] for sublist in album_tracks_data for id in sublist]
    name_songs = [name['track']['track_name'] for sublist in album_tracks_data for name in sublist]
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
        return " Invalid selection."
    print()

    attempts = 1
    while True:
      try:
        select_track = int(input("\n Get lyrics track #: "))
        track = select_index(select_track)
        if isinstance(track, int):
          track_id = id_map[track]
          track_name = name_map[track]
          lyrics_songs =  server.get_songs_by_lyrics(track_id)
          print("\n")
          print(f" Title: {track_name}")
          print("\n" + lyrics_songs['lyrics_body'])
          # print()
          # print(lyrics_songs)
        else:
          print(' invalid selection')
          if attempts > 3:
            song_lyrics()
            break
        option = int(input("\n [1] Select other track #:   [2] Exit\n Option: "))
        if option == 2:
          break
      except ValueError:
        print(" Invalid Selection!")
      attempts += 1
      
  while True:
    try:
      print_options()
      option = int(input("\n Option: "))
      if option == 1:
        print()
        print("" * 1, "-" * 53)
        print("  Ⱥdd Şongs Ⱥs Favorites")
        print("" * 1, "-" * 53)
        tracklist()
      elif option == 2:
        print("" * 1, "-" * 53)
        print(f"  Artist: {search_artist['artist']['artist_name']}")
        print(f"  Country: {search_artist['artist']['artist_country']}")
        print(f"  {len(artist_album)} Album")
        print("" * 1, "-" * 53)
        
        for idx, album in enumerate(album_name, start=1):
          count = idx + 1
          track = f"track{count}"
          track = Track(album)
          media.add_track(track)
      
        media.delay()
        album_list()
      elif option == 3:
        main()
      elif option == 4:
        favorite_sogns()
      elif option == 5:
        song_lyrics()
      elif option == 6:
        exit()
    except ValueError:
      print(" Invalid selection, please enter a number!.")
  
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
