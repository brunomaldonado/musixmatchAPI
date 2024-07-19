from random import randint
from utils.queueNode import Queue
from time import sleep
import threading
import time
import random
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

emojis = ['🔊', '🎼', '💽', '🎧', '🎵', '🎹', '🎶', '🎷', '🎸', '💿', '🎻', '🎙', '🪗', '🎤']

def print_intro(message, dot_count=6, dot_delay=0.25):
  random = randint(0, 5)
  play = ' '.join(map(str, emojis[random]))
  print(f".♩♪...♩.{play}", end="", flush=True)
  for _ in range(dot_count):
    print(".", end="", flush=True)
    time.sleep(dot_delay)
  print(" ", end="", flush=True)
  # print(message)

  for char in message:
    print(char, end="", flush=True)
    time.sleep(dot_delay)

def print_dots_after(width=46, dot_delay=0.525, duration=7):
  dots_num = int(duration / dot_delay)
  print(" ", end="", flush=True)
  for _ in range(dots_num):
    print(".", end="", flush=True)
    time.sleep(dot_delay)
  # print(" ok", flush=True)
  print(f"{bcolors.OKGREEN}ok{bcolors.ENDC}", flush=True)

# necesitamos instanciar canciones con la clase track
class Track:
  def __init__(self, title=None):
    self.title = title
    self.duration = randint(0, 1) # 5 o 6 seconds the play the songs

tracklist = []
class MediaPlayerQueue(Queue):  #va heredar del Queue que esta basado en nodes (programacion orientado a objetos)
  def __init__(self):
    super(MediaPlayerQueue, self).__init__()

  def add_track(self, track):
    self.enqueue(track.title)

  def delay(self):
    data = self.list_data()
    tracklist.append(data)
    list_size = len(self.list_data())
    # print(list_size)
    # ran_num = random.randint(1, list_size)
    # print(ran_num)
    if list_size < 3:
      sample_size = list_size
    else:
      sample_size = 3
    random_numbers = random.sample(range(1, list_size + 1), sample_size)
    # random_numbers = [4, 7, 2]
    sorted_numbers = sorted(random_numbers)
    # print(len(sorted_numbers))

    idx = 1
    while self.count > 0 and self.head is not None:
      current_track_node = self.dequeue()

      if idx <= list_size:
        if idx in sorted_numbers:
          # print("pause")
          self.print_node_with_delay(idx, current_track_node)
          # pass
          # self.print_track_with_pause(idx, current_track_node)
        else:
          # print("continue") 
          self.print_node_with_delay(idx, current_track_node)
        idx += 1


  
  def play(self):
    # message = f"Playing songs"
    # print_intro(message)
    # print(f"Count: {self.count}\n")
    new_data = tracklist[-1]
    # print(f"\ntracklist {new_data}\nlen {len(new_data)}")

    list_fav = self.list_data()
    # print(f"\nlist_fav {list_fav}\nlen {len(list_fav)}")

    indices = [new_data.index(item) + 1 for item in list_fav]
    # print(f"indices {indices}")
    # i = 23 # test
    i = 0
    while self.count > 0 and self.head is not None:
      current_track_node = self.dequeue()
      # print_track_title(idx, current_track_node)

      if i < len(indices):
        idx = i + 1
        if idx < 10:
          initial_spacing = " " * 1
          print(initial_spacing, end="", flush=True)
          index = f"{idx}"
        else:
          index = f"{idx}"
        
        if indices[i] < 10:
          spacing_after = " " * 0
          spacing_line = " "
          print(spacing_after, end="", flush=True)
          tracks = f"{indices[i]}{spacing_line}"
        else:
          spacing_line = ""
          tracks = f"{indices[i]}{spacing_line}"

        track = f"{index}  {tracks}" 
        self.print_title_with_delay(idx, track, current_track_node)
        i += 1

  def print_title_with_delay(self, idx, track, title, width=46, char_delay=0.0125):
    now_playing = emojis[(idx - 1) % len(emojis)]
    first_line_prefix = f"{track} {now_playing} "
    current_line = first_line_prefix
    empty_line = " " * (len(first_line_prefix) - 11)
    spacing_line = " " * 11
    words = title.split()
    title_lines = []
    initial_spacing = " " * 1


    for word in words:
      if len(current_line) + len(word) + 1 > width:
        title_lines.append(current_line.strip())
        current_line = empty_line + word + " "
      else:
        current_line += word + " "
  
    title_lines.append(current_line.strip())

    print(initial_spacing, end="", flush=True)
    # Print each line of the title with a delay
    for i, line in enumerate(title_lines):
      if i == 0:
        # Print the first line with the prefix
        # print(line, end="", flush=True)
        for char in line:
          print(char, end="", flush=True)
          time.sleep(char_delay)
      else:
        # Print subsequent lines with proper indentation
        # print("\n" + empty_line, end="", flush=True)
        print("\n" + spacing_line, end="", flush=True)
        # print("empty line", empty_line)
        for char in line[len(empty_line):]:
          print(char, end="", flush=True)
          time.sleep(char_delay)

      # If it's the last line of the title, print dots
      if i == len(title_lines) - 1:
        dot_thread = threading.Thread(target=print_dots_after, args=(width,))
        dot_thread.start()
        dot_thread.join()

  def print_node_with_delay(self, idx,  title, width=46, char_delay=0.0125):
    first_line_prefix = f"{idx} "
    # print(len(current_line))
    current_line = first_line_prefix
    empty_line = " " * (len(first_line_prefix) - 4)
    title_lines = []
    spacing_line = " " * 3
    initial_spacing = " " * 1
    
    for word in title.split():
      if len(current_line) + len(word) + 1 > width:
        title_lines.append(current_line.strip())
        current_line = empty_line + word + " "
      else:
        current_line += word + " "
    title_lines.append(current_line.strip())
    
    # print each line of the title with a delay
    print("\n", initial_spacing, end="", flush=True)
    for i, line in enumerate(title_lines):
      if i == 0:
        for char in line:
          print(char, end="", flush=True)
          time.sleep(char_delay)
      else:
      # print subsequent lines with proper identation
        print("\n", spacing_line, end="", flush=True)
        for char in line[len(empty_line):]:
          print(char, end="", flush=True)
          time.sleep(char_delay)


  def print_track_with_pause(self, idx,  title, width=46, char_delay=0.0125):
    first_line_prefix = f"{idx} "
    # print(len(current_line))
    current_line = first_line_prefix
    empty_line = " " * (len(first_line_prefix) - 5)
    title_lines = []
    spacing_line = " " * 4
    initial_spacing = " " * 1
    
    for word in title.split():
      if len(current_line) + len(word) + 1 > width:
        title_lines.append(current_line.strip())
        current_line = empty_line + word + " "
      else:
        current_line += word + " "
    title_lines.append(current_line.strip())
    
    # print each line of the title with a delay
    print("\n", initial_spacing, end="", flush=True)
    for i, line in enumerate(title_lines):
      if i == 0:
        for char in line:
          print(char, end="", flush=True)
          time.sleep(char_delay)
      else:
      # print subsequent lines with proper identation
        print("\n", spacing_line, end="", flush=True)
        for char in line[len(empty_line):]:
          print(char, end="", flush=True)
          time.sleep(char_delay)
      
      # If it's the last line of the title, print dots
      if i == len(title_lines) - 1:
        dot_thread = threading.Thread(target=print_dots_after, args=(width,))
        dot_thread.start()
        dot_thread.join()

def main():
  media = MediaPlayerQueue()
  #media = MediaPlayerQueue()
  #print("hello world")
  print()
  print("-" * 99)
  # print_intro("Playing songs")
  
  list_songs = ['Beautiful Things', 'Sonido Machacas - Acatepec Guerrero Mexico y United State-New York (Pal ft Sain R. Isis Burm K. JJ) England Fix (Live - Streaming)', 'Country Road - Mountain (Tk fy AI)', 'Trabajo Por Mi Cuenta C - Los Tigres del Norte (Isis Bumr ft R.)', 'Zombie', 'When September Ends', 'Memories', 'Love You', 'W. T. F.', 'Beautiful Eyes', 'Fly', 'Mothers Daughter X Boys Dont Cry (feat. Anitta) - Live', 'Angels Like You', 'Edge of Midnight (Midnight Sky Remix) [feat. Stevie Nicks]', 'Zombie (Live from the NIVA Save Our Stages Festival)', 'Plastic Hearts']

  #list_songs = ['Perfect', 'Trabajo Por Mi Cuenta C - Los Tigres del Norte (Isis Bumr ft R.)', 'Beautiful Things']
  print("\n")

  for idx, song in enumerate(list_songs):
    # print(f"{idx + 1} {song}")
    count = idx + 1
    track = f"track{count}"
    track = Track(song)
    media.add_track(track)


  track1 = Track('Love Me Again')
  # track2 = Track('Dame Una Noche')
  # track3 = Track('Soy Y Sere')
  # track4 = Track('Fanatica Sensual')
  # track5 = Track('Love and Sex')
  # track6 = Track('No Quiero Que Te Vayas')
  # track7 = Track('Fanatica Sensual')

  media.add_track(track1)
  # media.add_track(track2)
  # media.add_track(track3)
  # media.add_track(track4)
  # media.add_track(track5)
  # media.add_track(track6)
  # media.add_track(track7)

  media.play()
if __name__ == '__main__':
  main()
