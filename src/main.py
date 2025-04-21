from utils import server
from utils.mediaPlayer import Track, MediaPlayerQueue, starting_message, print_radio_art
from utils.config import content_data, list_favorite_songs, media_songs_list, list_favorite_artists, list_artists_countries, indentation_title1, indentation_title2, indentation_title3
import random
import textwrap

def print_options():
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
  
  artist_name = {search_artist['artist']['artist_name']}
  artist = list(artist_name)[0]

  print("" * 1, "-" * 53)
  print(f"  Artist: {artist}")
  country = search_artist['artist']['artist_country']
  if not str(country).strip():
    artist_country = f"UK"
  else:
    artist_country = country
  print(f"  Country: {artist_country}")
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
  # print()

  songs_list = []
  print_songs_list = []
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

    # print(f"song_list\n {songs_list}\n\n")
    media_songs_list.append(songs_list)
    content_data.append(songs_list)

    for song in print_songs_list:
      if print_songs_list.count(song) > 1:
        print_songs_list.remove(song)
  
    for idx, song in enumerate(print_songs_list, start=1):
      count = idx + 1
      track = f"track{count}"
      track = Track(song)
      media.add_track(track)
    
    media.delay()
    print()
    
    def select_index(selection):
      if 1 <= selection <= len(print_songs_list):
        return selection - 1
      else:
        return " Invalid Selection"
    
    print()
    
    attempts = 1
    while True:
      try:
        selection = int(input("\n Selected song # to add: "))
        add_song = select_index(selection)
        if isinstance(add_song, int):
          list_favorite_songs.append(songs_list[add_song])
          list_favorite_artists.append(search_artist['artist']['artist_name'])
          list_artists_countries.append(artist_country) 

          if list_favorite_songs.count(songs_list[add_song]) > 1:
            print(" This song has been added recently...")
          else:
            continue

        else:
          print(" Enter a number of song to add.")
          if attempts > 3:
            tracklist()
            break
        option = int(input("\n [1] Selected song #   [2] Exit\n Option: "))

        if option == 2:
          break
      except ValueError:
        print(" Invalid selection. Please enter a number.")
      attempts += 1


  album_tracks_data = []
  artist_album_tracks_data = []
  artist_album_tracks_data.append(album_tracks_data)
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
          print()
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
            name_songs = track['track']['track_name']
            artist_song = f"{artist} - {name_songs}"
            # album_tracks.append(artist_song)
            album_tracks.append(track['track']['track_name'])
            songs_list.append(artist_song)
            print_songs_list.append(track['track']['track_name'])

          for idx, name in enumerate(album_tracks, start=1):
            count = idx + 1
            track = f"track{count}"
            track = Track(name)
            media.add_track(track)

          media.delay()
          print("\n")
          break
        else:
          print(" Please enter a number of albums.")
      except ValueError:
        print(" Invalid Selection!. Please enter a number.")
  
  album_list()

  def favorite_sogns():
    my_dict = {}
    artist_list = []
    for artist, country in zip(list_favorite_artists, list_artists_countries):
      my_dict[artist] = country
      a_c = f"{artist} ({country})"
      artist_list.append(a_c)
    
    # print(f"\n{my_dict}\n{artist_list}")

    unique_artists = []
    for artist in artist_list:
      if artist not in unique_artists:
        unique_artists.append(artist)

    artists = ', '.join(list(unique_artists))
    # print(artists)

    random_number = random.randint(2, 4)
    # print(random_number)
    song_genre = ['Pop', 'Ambient', 'Alternative', 'Dance']

    if len(unique_artists) <= 2:
      list_song_genres = random.sample(song_genre, 1)
    else:
      list_song_genres = random.sample(song_genre, random_number)
    # print(list_song_genres)
    gender_list = ', '.join(list_song_genres)
    # print(gender_list)

    if len(list_favorite_songs) == 0:
      print("" * 1, "-" * 53)
      print("  ⭐️ Favourite Songs")
      print("" * 1, "-" * 53)
      print()

      print("             Ɲo Ş🎧ngs Ⱥdded Ⱥs Favorites")
      print("\n")
    else:
      print("" * 1, "-" * 53)
      print("  ⭐️ Favourite S🎧ngs")
      print(f"  Artists: {indentation_title3(artists)}")
      print(f"\n  {gender_list}")
      print("" * 1, "-" * 53)
      print()

      message1 = f".♪..♩...🎼.♩♪...♩ Play"
      radio_art1 = [
          "╔═══╗",
          "║███║",
      ]

      print_radio_art(radio_art1)
      starting_message(message1)

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
      print()

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
    # print(artist_album_tracks_data)
    
    id_songs = [id['track']['track_id'] for sublist in album_tracks_data for id in sublist]
    name_songs = [name['track']['track_name'] for sublist in album_tracks_data for name in sublist]
    # print(f"\nid_songs\n{id_songs}\nname_songs\n{name_songs}")

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

    my_dict = {}
    singer_song = []

    for singer, song in zip(artist, single_names):
      my_dict[singer] = song
      a_s = f"{artist} - {song}"
      singer_song.append(a_s)
    
    singer_song.extend(list_favorite_songs)
    # print(singer_song)

    seen_song = set()
    unique_values = []

    for name in singer_song:
      if name not in seen_song:
        seen_song.add(name)
        unique_values.append(name)
    
    # for idx, song in enumerate(unique_values, start=1):
    #   print(f"{idx} {song}")

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
          # print(f"\n\nlyriscs song {lyrics_songs}\n\n")
          # print("\n")
          # print(f"  {track_name}\n")
          # print()
          # for line in lyrics_songs['lyrics_body'].split("\n"):
          #   if '**' not in line and not line.strip().isdigit() and not line.strip().startswith('(') and not line.strip().endswith(')'):
          #     print(line)
          # print("\n" + lyrics_songs['lyrics_body'])
          spacing_line = " " * 2
          max_width = 50
          print("\n")
          title = f"{track_name}"
          wrapped_title = textwrap.wrap(title, max_width)

          for line in wrapped_title:
            underline = "˜" * len(line)
            print(f"{spacing_line}{line}")
            print(f"{spacing_line}{underline}")
          print()

          for line in lyrics_songs['lyrics_body'].split("\n"):
            line = line.strip()

            if not line:
              print()
              continue

            if ('**' in line) or line.isdigit() or line.startswith('(') or line.endswith(')'):
              continue

            wrapped_lines = textwrap.wrap(line, width=max_width)

            for wrapped_line in wrapped_lines:
              print(f"{spacing_line}{wrapped_line}")

          print()
        else:
          print(' Please enter a number of lyrics songs.')
          if attempts > 3:
            song_lyrics()
            break
        option = int(input("\n [1] Select other track #:   [2] Exit\n Option: "))
        if option == 2:
          break
      except ValueError:
        print(" Invalid Selection!. Please enter a number.")
      attempts += 1
      
  while True:
    try:
      print()
      print_options()
      option = int(input("\n Option: "))
      if option == 1:
        print()
        print("" * 1, "-" * 53)
        print("  Ⱥdd Şongs Ⱥs Favorites")
        print("" * 1, "-" * 53)
        tracklist()
        print()
      elif option == 2:
        print()
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
        print()
        media_songs_list.clear()
        main()
      elif option == 4:
        print()
        favorite_sogns()
        print()
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

