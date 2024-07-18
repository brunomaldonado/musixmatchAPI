# num_id = [64798455, 65235590, 64798443, 63626195, 61993940, 28413177, 28261313, 28235206, 58002669, 13873823]

# # Function to return index 0 if input is 1
# def select_index(selection):
#     if 1 <= selection <= len(num_id):
#         return num_id[selection - 1]
#     else:
#         return "Invalid selection"

# # Test the function
# selection = int(input("input number: "))
# result = select_index(selection)
# print(result) 

import random
import time

list_songs = ['Square Biz.', 'Candy Remix Parte 2 (feat. Tempo & Arcangel)', 'Fanática Sensual - Remix', 'Candy', 'Feel', 'Choca', "Pa'l Piso", 'Fanatica Sensual', 'El Matadero', 'No Quiero Que Te Vayas', 'Mi Vecinita', 'Juegas Con Mi Mente', 'Donde Los Consigo?', 'Soy Y Sere', 'Coquetea', 'Zapatito Roto', 'Dame Una Noche', 'Satiro', 'Love and Sex']
list_size = len(list_songs)
ran_num = random.randint(1, list_size)
print(ran_num)

favourite_song = []
# def print_tracks():
def print_tracks():
    for idx, song in enumerate(list_songs):
        print(f"{idx + 1} {song}")

def select_index(selection):
    if 1 <= selection <= len(list_songs):
        return selection - 1
    else:
        return "Invalid Selection"

print_tracks()

# while True:
#     selection = int(input("\nSelect # song to add: "))
#     add_song = select_index(selection)
#     if isinstance(add_song, int):
#         favourite_song.append(list_songs[add_song])
#     else:
#         print("invalid selection")
#     option = int(input("\n1.- continue    2.- exit\nOption: "))
#     if option == 2:
#         break
# print()
seen = set()
result = []
for item in favourite_song:
    if item not in seen:
        seen.add(item)
        result.append(item)
    else:
        if result.count(item) < 1:
            result.append(item)
print()
emojis = ['🎷', '💽', '🎹','🎧', '🎺', '🔊']
for idx, item in enumerate(result, start=1):
    emoji = emojis[(idx - 1) % len(emojis)]
    print(f"{idx:2} {emoji} {item}")


def indentation_word(title, width=46, char_delay=0):
  print(" " * 1, "-" * 53)
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 1
  initial_spacing = " " * 1

  for word in title.split():
    if len(current_line) + len(word) + 1 > width:
      title_lines.append(current_line.strip())
      current_line = empty_line + word + " "
    else:
      current_line += word + " "
    
  title_lines.append(current_line.strip())
#   print(title_lines)
  print("\n", initial_spacing, end="", flush=True)
  for i, line in enumerate(title_lines):
    if i == 0:
      for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    else:
      print("\n", spacing_line, end="", flush=True)
      for char in line[len(empty_line):]:
        print(char, end="", flush=True)
        time.sleep(char_delay)    
    
title = " ℗ 2023 Smiley Miley, Inc. under exclusive license to Columbia Records, a Division of Sony Music Entertainment"
indentation_word(title)


"""
for word in words:
    if len(current_line) + len(word) + 1 > width:
      print(current_line)
      if first_line:
        current_line = " " * (len(str(idx)) + 6) + word + " "
        first_line = False
      else:
        current_line = " " * 6 + word + " "
    else:
      current_line += word + " "
  
  print(current_line, end="", flush=True)
"""


# data = [["Don't Need to Sleep", 'LEGEND (Solo Piano Version)', 'LEGEND (Solo Sessions) - EP', 'Nervous (Remixes)', 'LEGEND', 'Honey', 'Dope (feat. JID) - Single', 'FREE', 'You Deserve It All', 'Bigger Love'], ['FREE'], ["Don't Need to Sleep", 'LEGEND (Solo Piano Version)', 'LEGEND (Solo Sessions) - EP', 'Nervous (Remixes)', 'LEGEND', 'Honey', 'Dope (feat. JID) - Single', 'FREE', 'You Deserve It All', 'Bigger Love'], ['You Deserve It All'], ["Don't Need to Sleep", 'LEGEND (Solo Piano Version)', 'LEGEND (Solo Sessions) - EP', 'Nervous (Remixes)', 'LEGEND', 'Honey', 'Dope (feat. JID) - Single', 'FREE', 'You Deserve It All', 'Bigger Love'], ['Honey (Piano Version)', 'Nervous (Piano Version)', 'Wonder Woman (Piano Version)', 'One Last Dance (Piano Version)', 'Bridge Over Troubled Water'], ['FREE', 'You Deserve It All', 'Honey (Piano Version)', 'Nervous (Piano Version)', 'Wonder Woman (Piano Version)', 'One Last Dance (Piano Version)', 'Bridge Over Troubled Water'], ["Don't Need to Sleep", 'LEGEND (Solo Piano Version)', 'LEGEND (Solo Sessions) - EP', 'Nervous (Remixes)', 'LEGEND', 'Honey', 'Dope (feat. JID) - Single', 'FREE', 'You Deserve It All', 'Bigger Love'], ['Dope (feat. JID)'], ["Don't Need to Sleep", 'LEGEND (Solo Piano Version)', 'LEGEND (Solo Sessions) - EP', 'Nervous (Remixes)', 'LEGEND', 'Honey', 'Dope (feat. JID) - Single', 'FREE', 'You Deserve It All', 'Bigger Love'], ['Honey (Piano Version)', 'Nervous (Piano Version)', 'Wonder Woman (Piano Version)', 'One Last Dance (Piano Version)', 'Bridge Over Troubled Water'], ['FREE', 'You Deserve It All', 'Dope (feat. JID)', 'Honey (Piano Version)', 'Nervous (Piano Version)', 'Wonder Woman (Piano Version)', 'One Last Dance (Piano Version)', 'Bridge Over Troubled Water']]
# data =  [['Maggie', 'Memories', 'Venom', 'Zombie'],['Angela'],['Apple', 'Orange'],['Solarize', 'Hysteresis', 'Mystified', 'Feel', 'Numb', 'Live Me Again']]

# return the kast index data, no matter how long the list
# new_data_is = data[-1]
# print("\nlist data", data)
# print("\ndata len", len(data))
# print("\nnew data", new_data_is)
# print("\nnew_data len", len(new_data_is))

# list1 = ['Nervous - Xan Griffin Remix', 'Nervous - Prince Fox Remix', 'Nervous - King Britt Sexytech Remix', "Don't Need to Sleep", 'You Deserve It All', 'Ooh Laa', 'Actions', 'I Do', 'One Life', 'Wild (feat. Gary Clark Jr.)', 'Bigger Love', 'U Move, I Move (feat. Jhene Aiko)', 'Favorite Place', 'Slow Cooker', 'Focused', 'Conversations in the Dark', "Don't Walk Away (feat. Koffee)", 'Remember Us (feat. Rapsody)', "I'm Ready (feat. Camper)", 'Always', 'Never Break', 'Honey (Piano Version)', 'Nervous (Piano Version)', 'Wonder Woman (Piano Version)', 'One Last Dance (Piano Version)', 'Bridge Over Troubled Water']

# list2 =  ['I Do', 'Focused', 'Bridge Over Troubled Water']
print("\n")
num1  = 45
num2 = 2
idx = 13
spacing  = " " * 1
# if idx < 10:
first_line_prefix = f"{spacing}{num2}  {idx}  Love Me Again"
# else:
#   first_line_prefix = f"{num1}"

print(num1)
print(first_line_prefix)  




