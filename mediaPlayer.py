from random import randint
from queueNode import Queue
from time import sleep
import threading
import time
import random
import secrets
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

# def print_dots_after(dot_delay=0.375, duration=6):
#     num_dots = int(duration / dot_delay)
#     for _ in range(num_dots):
#       print(".", end="", flush=True)
#       time.sleep(dot_delay)
#     # print(" ok")
#     print(f"{bcolors.OKGREEN} ok{bcolors.ENDC}", flush=True)

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

# def print_dots_after(width=29, dot_delay=0.375, duration=6):
#     # total_space = width - len(title) - len("  🎧 ") - len("✓")
#     # num_dots = total_space
#     # dots = "." * num_dots
#     num_dots = int(duration/ dot_delay)

#     for _ in range(num_dots):
#       print(".", end="", flush=True)
#       time.sleep(dot_delay)
#     print("", end="", flush=True)
#     # print(dots + "✓", flush=True)
#     print(f"{bcolors.OKGREEN} ok{bcolors.ENDC}", flush=True)

def print_dots_after(width=46, dot_delay=0.525, duration=7):
  # remaining_space = width - title_length - 6  # 6 is for the fixed prefix length and " ok"
  # dots = "." * remaining_space
  dots_num = int(duration / dot_delay)
  print(" ", end="", flush=True)
  for _ in range(dots_num):
    print(".", end="", flush=True)
    time.sleep(dot_delay)
  # print(" ok", flush=True)
  print(f"{bcolors.OKGREEN}ok{bcolors.ENDC}", flush=True)


# def print_dots(messages, dot_count=6, dot_delay=0.225, emoji="🎧"):
#     for number, message in enumerate(messages, start=1):
#       num = f"{number:2}"
#       print(f"{num} {emoji}", end="", flush=True)
#       for _ in range(dot_count):
#           print(".", end="", flush=True)
#           time.sleep(dot_delay)
      
#       print(" ", end="", flush=True)
#       print(message)
    
  # for number, message in enumerate(messages, start=1):
  #   num = f"{number:2}"
  #   # dot_str = "." * dot_count
  #   # first_part = f"  {num} {emoji}{dot_str}"
  #   print(f"{num} {emoji}", end="", flush=True)
  #   for _ in range(dot_count):
  #     print(".", end="", flush=True)
  #     time.sleep(dot_delay)
  #   print(" ", end="", flush=True)
  #   # print(message)

  #   # Calculate remaining width for the message after first_part
  #   first_part_length = len(f"{num} {emoji}") + dot_count + 1
  #   remaining_width = terminal_width - first_part_length

  #   words = message.split()
  #   line = ""
  #   lines = []
  #   for word in words:
  #     if len(line) + len(word) + 1 <= remaining_width:
  #       line += " " + word if line else word
  #     else:
  #       lines.append(line)
  #       line = word
    
  #   lines.append(line)
  #   print(lines[0])

  #   # print(f"{first_part} {lines[0]}")
  #   # # time.sleep(dot_delay * dot_count)

  #   for line in lines[1:]:
  #     print(" " * initial_spacing + line)
    
  #   time.sleep(0.125)



# if __name__ == "__main__":
#     print_dots("Macarena")
#     print_dots("Bamba")

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
  
  def data(self):
    # number = []
    if self.count > 0 and self.head is not None:
      list = self.list_data()
      print(list)
      # ran_num = random.randint(1, num)
      # number.append(ran_num)
      # print(f"pause {ran_num}")
    # return number
      

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
    # if idx == list_size:
    #     print("pause")
    # print(sorted_numbers)
    # for idx in range(1, list_size + 1):
    #   if idx in sorted_numbers:
    #     print("pause")
    #   else:
    #     print("continue") 
    idx = 1
    while self.count > 0 and self.head is not None:
      current_track_node = self.dequeue()
      # print(f"  {idx:2} {current_track_node}")
      # idx += 1 
      # if idx == ran_num:
      #   self.print_track_with_pause(idx, current_track_node)
      # else:
      #   self.print_node_with_delay(idx, current_track_node)
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
    # track = i
    # while i < len(indices):
    #   print(indices[i])
    #   i += 1
    idx = 1
    print("Track")
    while self.count > 0 and self.head is not None:
      current_track_node = self.dequeue()
      # print_track_title(current_track_node, idx)
      # message = f"  🎧 {current_track_node} "
      # dot_thread = threading.Thread(target=print_dots_after, args=(current_track_node,))
      # dot_thread.start()
      # dot_thread.join()
      # idx += 1
      # i = 0

      if i < len(indices):
        if indices[i] < 10:
          spacing = " " * 1
          print(spacing, end="", flush=True)
          track = f"{indices[i]}"
        else:
          track = f"{indices[i]}"

        self.print_title_with_delay(track, idx, current_track_node)
        i += 1
        idx += 1
  
  # def print_title_with_delay(self, title, idx, width=46, char_delay=0.0125):
  #   words = title.split()
  #   num = f"{idx:2}"
  #   first_line_prefix = f"{num} 🎧 "
  #   current_line = first_line_prefix
  #   empty_line = " " * len(first_line_prefix)
  #   first_line = True

  #   for word in title.split():
  #     if len(current_line) + len(word) + 1 > width:
  #       print(current_line)
  #       current_line = empty_line + word + " "
  #     else:
  #       current_line += word + " "
    
  #   remaining_space = width - len(current_line) - len(" ok")
  #   dots = "." * remaining_space
  #   print(current_line + dots + " ok")
      

  def print_title_with_delay(self, track, idx, title, width=46, char_delay=0.0125):
    # print(tracklist)
    # new_data = tracklist[-1]
    # print(f"\ntracklist {new_data}\nlen {len(new_data)}")
    # list_fav = self.list_data()
    # print(f"\nlist_fav {list_fav}\nlen {len(list_fav)}")
    # indices = [new_data.index(item) + 1 for item in list_fav]
    # print(f"indices {indices}")
    # track = 16
    now_playing = emojis[(idx - 1) % len(emojis)]
    # now_playing = "🎧"
    if idx < 10:
      space = " " * 1
      first_line_prefix = f"{track}  {space}{idx} {now_playing} "
    else:
      first_line_prefix = f"{track}  {idx} {now_playing} "
    # add = " " if idx < 10 else ""
    # first_line_prefix = f"{add}{track}  {idx} {now_playing} "
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

  # Print each character with a delay
    # for line in title_lines:
    #   for char in line:
    #     print(char, end="", flush=True)
    #     time.sleep(char_delay)
        
    # for word in title.split():
    #   if len(current_line) + len(word) + 1 > width:
    #     print(current_line)
    #     current_line = empty_line + word + " "
    #   else:
    #     current_line += word + " "
    #     title_length += len(word) + 1

    # print(current_line, end="", flush=True)
    # for char in current_line[len(first_line_prefix):]:
    #   print(char, end="", flush=True)
    #   time.sleep(char_delay)
    # dot_thread = threading.Thread(target=print_dots_after, args=(width,))
    # dot_thread.start()
    # dot_thread.join()

    # if self.count > 0 and self.head is not None:
    #   messages = self.list_data()

    #   seen = set()
    #   result = []
    #   for item in messages:
    #     if item not in seen:
    #       seen.add(item)
    #       result.append(item)
    #     else:
    #       if result.count(item) < 1:
    #         result.append(item)
      
    #   print_dots(result)


# def print_track_title(title, idx, width=46, start=1):
  # words = title.split()
  # num = f"{idx:2}"
  # current_line = f" {num} 🎧 "
  # first_line = True
  # for word in words:
  #   if len(current_line) + len(word) + 1 > width:
  #     print(current_line)
  #     if first_line:
  #       current_line = " " * (len(str(idx)) + 6) + word + " "
  #       first_line = False
  #     else:
  #       current_line = " " * 6 + word + " "
  #   else:
  #     current_line += word + " "
  
  # print(current_line, end="", flush=True)


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

  
  """
  1 🎧 Beautiful Things ..................ok
  2 🎧 Sonido Machacas - Acatepec Guerrero 
     Mexico y United State-New York (Pal ft 
     Sain R. Isis Burm K. JJ) England Fix 
     (Live - Streaming) ............... ok
  3 🎧 Country Road .................... ok



  1 🎧 Trabajo Por Mi Cuenta C - Los Tigres del 
     R.) ............ ✓
     AI) ............ ✓
     Zombie ............ ✓
 4 🎧 Sonido Machacas - Acatepec Guerrero 
      Mexico y United State-New York (Pal ft 
      Sain R. Isis Burm K. JJ) England Fix 
      Streaming) ............ ✓
     Ends ............ ✓
  """