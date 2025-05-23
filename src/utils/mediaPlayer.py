from time import sleep
import threading
import time
from random import randint
import random
import sys
from pathlib import Path
import time
import textwrap
from colorama import Style

src_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(src_dir))

from utils.queueNode import Queue
from utils.config import content_data, example, media_songs_list

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

emojis = ['🔊', '🎧', '💽', '🎵', '🎻', '🎷', '🪗', '🎸', '💿', '🎹', '🎼', '🪗', '🎤']
random = randint(0, 5)
play = ' '.join(map(str, emojis[random]))
message1 = f".♪..♩...{play}.♩♪...♩ Play"
message2 = r"""ng Playl"""
message3 = r"""st......║(O)║♩ ♫ ♪ ♫"""

radio_art1 = [
  "╔═══╗",
  "║███║",
]
radio_art2 = [
  "st...♩♪.║(O)║♩ ♫ ♪ ♫",
  "╚═══╝"
]

# art4 = r"""    ╚═══╝"""

def spinner_letter(letter, letter_i="ɨ"):
  spinner_chars = ['-', '\\', '♪', '♩']

  for frame in spinner_chars:
    sys.stdout.write(f"\r{letter}{frame}")
    sys.stdout.flush()
    time.sleep(0.25)
  # sys.stdout.write(f"\r{letter}{bcolors.OKGREEN}i{bcolors.ENDC}")
  sys.stdout.write(f"\r{letter}{letter_i}")
  sys.stdout.flush()


def print_characters_after(title, dot_count=0, dot_delay=0.25):
  for _ in range(dot_count):
    print(".", end="", flush=True)
    time.sleep(dot_delay)
  print("", end="", flush=True)

  for char in title:
    print(char, end="", flush=True)
    time.sleep(dot_delay)
                                    #46
def print_radio_art(art_lines, indent=42, width=46, char_delay=0.25):
  spacing = " " * indent

  for line in art_lines:
    print(spacing, end="", flush=True)
    for char in line:
      print(char, end="", flush=True)
      time.sleep(char_delay)
    print()

def starting_message(title, width=46, char_delay=0.25):
  current_line = " "
  title_lines = []
  spacing_line = " " * 2

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = word + " "
    else:
      current_line += word + " "
  title_lines.append(current_line.strip())

  # print each line of the title with a delay
  print(f"{spacing_line}", end="", flush=True)
  for i, line in enumerate(title_lines):
    if i == 0:
      for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    else:
      # print subsequent lines with proper identation
      for char in line.strip():
        print(char, end="", flush=True)
        time.sleep(char_delay)

  last_line = title_lines[-1]
  last_line1 = message2[-1]

  if len(title_lines) == 1:
    spinner_letter(f"{spacing_line}{last_line}")
    print_characters_after(message2)
    #print(f"--")
    spinner_letter(f"{spacing_line}{message1}i{message2[:-1]}{last_line1}")
    print_characters_after(message3)
    print()
    print_radio_art(radio_art2[1:])
    # print(f"\n{initial_space}{art4}")

def play_spinner(song):
  spinner = ['🔊', '-', '\\', '♪', '♩', ' ', '-', '\\', '♪', '♩', ' ']
  for frame in spinner:
    sys.stdout.write(f'\r{song} {frame} ')
    sys.stdout.flush()
    time.sleep(.25)
  sys.stdout.write(f'\r{song} \n')
  sys.stdout.flush()


def print_dots_after(width=46, dot_delay=0.525, duration=7):
  dots_num = int(duration / dot_delay)
  print(" ", end="", flush=True)
  for _ in range(dots_num):
    print(".", end="", flush=True)
    time.sleep(dot_delay)
  print(" ok", flush=True)
  #print(f"{bcolors.OKGREEN}ok{bcolors.ENDC}", flush=True)


# necesitamos instanciar canciones con la clase Track
class Track:
  def __init__(self, title=None):
    self.title = title
    self.duration = randint(0, 1) # 5 o 6 seconds the play the songs

# example = []
class MediaPlayerQueue(Queue):  #va heredar del Queue que esta basado en nodes (programacion orientado a objetos)
  def __init__(self):
    super(MediaPlayerQueue, self).__init__()

  def add_track(self, track):
    self.enqueue(track.title)

  def delay(self):
    list_size = len(self.list_data())
    # print(f"LIST SIZE\n{list_size}")

    if list_size < 3:
      sample_size = list_size
    else:
      sample_size = 3
    # random_numbers = random.sample(range(1, list_size + 1), sample_size)
    # random_numbers = [4, 7, 2]
    # sorted_numbers = sorted(random_numbers)
    # print(len(sorted_numbers))

    idx = 1
    i =0
    while self.count > 0 and self.head is not None:
      current_track_node = self.dequeue()
      # print(idx, current_track_node)
      self.print_node_with_delay(idx, current_track_node)
      idx += 1

  def play(self):
    # print(f"\n\nCONTENT DATA {content_data}\nlen {len(content_data)}\n")

    if len(content_data) == 0:
      current_list = example
    else:
      current_list = content_data

    favorites_list = self.list_data()

    # print(f"\n\ncurrent_list\n {current_list}\nlen {len(current_list)}\n\n")
    # print(f"favorite_list\n {favorites_list}\n")

    unique_songs_list = []
    seen1 = set()

    for sublist in media_songs_list:
      item = tuple(sublist)
      if item not in seen1:
        seen1.add(item)
        unique_songs_list.append(sublist)

    # print(f"\nunique_songs_list\n {unique_songs_list}\n\nlen {len(unique_songs_list)}")

    unique_content_data = []
    seen2 = set()

    for sublist in current_list:
      item = tuple(sublist)
      if item not in seen2:
        seen2.add(item)
        unique_content_data.append(sublist)

    final_current_list = []
    seen_sublist = set()

    for sublist in unique_content_data:
      not_in_songs_list = [item for item in sublist if item not in unique_songs_list]
      in_songs_list = [item for item in sublist if item in unique_songs_list]

      if tuple(not_in_songs_list) and tuple(not_in_songs_list) not in seen_sublist:
        final_current_list.append(not_in_songs_list)
        seen_sublist.add(tuple(not_in_songs_list))
      if tuple(in_songs_list) and tuple(in_songs_list) not in seen_sublist:
        final_current_list.append(in_songs_list)
        seen_sublist.add(tuple(in_songs_list))

    current_list = final_current_list
    # print(f"\ncurrent_list\n {current_list}\n\nlen {len(current_list)}")
    # print(f"\nfavorite_list\n {favorites_list}\n")

    last_sublist = current_list[-1]
    indices = []

    for item in favorites_list:
      if item in last_sublist:
        indices.append(last_sublist.index(item) + 1)
      else:
        for sublist in current_list:
          if item in sublist:
            indices.append(sublist.index(item) + 1)
            break

    # for sublist1 in unique_songs_list:
    #   for sublis2 in current_list:
    #     if sublist1 == sublis2:
    #       print("is equal")

    # print(f"\nindices {indices}\n\n")

    # idx = 1
    i = 0
    while self.count > 0 and self.head is not None:
      current_track_node = self.dequeue()
      # print(idx, current_track_node)
      # idx += 1
      spacing_after = " " * 1
      spacing_line = " "
      if i < len(indices):
        idx = i + 1
        if idx < 10:
          index = f"{spacing_line}{idx}{spacing_after}"
        else:
          spacing_line = ""
          index = f"{spacing_line}{idx}{spacing_after}"

        if indices[i] < 10:
          spacing_line = " " * 1
          tracks = f"{spacing_line}{indices[i]}"
        else:
          spacing_line = ""
          tracks = f"{indices[i]}{spacing_line}"

        track = f"{bcolors.OKCYAN}{index}{bcolors.ENDC}{tracks}"

        # print(track, current_track_node)
        self.print_title_with_delay(idx, track, current_track_node)
        i += 1


  def print_title_with_delay(self, idx, track, title, max_width=63, char_delay=0.0125):
    now_playing = emojis[(idx - 1) % len(emojis)]
    initial_line = " " * 1
    #first_line = f"{track} {now_playing} {title}"
    line_length = len(f"{initial_line}{track} {now_playing} ")
    #current_line = first_line
    spacing_line = " " * 9

    wrapped_text = textwrap.wrap(title, width=max_width - line_length)
    if wrapped_text:
      f = f"{track} {now_playing} {wrapped_text[0]}"
      formatted_text = f
      if len(wrapped_text) > 1:
        formatted_text += "\n" + "\n".join(spacing_line + line for line in wrapped_text[1:])

      for char in formatted_text:
        print(char, end="", flush=True)
        time.sleep(char_delay)

      last_line =f"{wrapped_text[-1]}"
      if len(wrapped_text) > 1:
        play_spinner(f"{spacing_line}{last_line}")
      else:
        #print(len(last_line))
        f_t = f"{track} {now_playing} {last_line}"
        play_spinner(f_t)
    else:
      return None

  def print_node_with_delay(self, idx, title, max_width=63, char_delay=0.0125):
    if idx < 10:
      spacing_after = " " * 0
      initial_spacing = " "
      print(spacing_after, end="", flush=True)
      index = f"{initial_spacing}{idx}"
    else:
      initial_spacing = " "
      index = f"{idx}"

    first_line_prefix = f"{bcolors.OKCYAN}{index}{bcolors.ENDC} {title}"
    # print(len(current_line))
    current_line = first_line_prefix
    spacing_line = " " * 4
    initial_line = " " * 1

    wrapped_text = textwrap.wrap(current_line, width=max_width)
    if wrapped_text:
      formatted_text = f"{initial_line}{wrapped_text[0]}"
      if len(wrapped_text) > 1:
        formatted_text += "\n" + "\n".join(spacing_line + line for line in wrapped_text[1:])

      for char in formatted_text:
        print(char, end="", flush=True)
        time.sleep(char_delay)

      print("\n", end="", flush=True)

    else:
      return None


def main():
  media = MediaPlayerQueue()
  print()
  print(" " * 1, "-" * 53)

  # print_radio_art(radio_art1)
  # starting_message(message1)

  songs = ['Simple Plan - Can not Keep My Hands Off You - feat. Rivers Cuomo', 'Sonido Machacas - Acatepec Guerrero Mexico y United State-New York (Pal ft Sain R. Isis Burm K. JJ) England Fix (Live - Streaming)', 'Stay Alive']
  print()
  for idx, song in enumerate(songs):
    # print(f"{idx + 1} {song}")
    count = idx + 1
    track = f"track{count}"
    track = Track(song)
    media.add_track(track)
  print()

  track1 = Track('Beautiful Things')
  track2 = Track('Simple Plan - Can not Keep My Hands Off You - feat. Rivers Cuomo')



  media.play()
if __name__ == '__main__':
  main()
