import random
import time
import sys
nested_list = [['a', 'b'], ['g', 'w', 's']]

# Convertir la lista anidada en una sola lista
flat_list = [item for sublist in nested_list for item in sublist]

# print(flat_list)
example = [['Beautiful Things', 'Sonido Machacas - Acatepec Guerrero Mexico y United State-New York (Pal ft Sain R. Isis Burm K. JJ) England Fix (Live - Streaming)', 'Country Road', 'Love and Sex', 'Zombie', 'When September Ends', 'Memories', 'Love You', 'W. T. F.', 'Beautiful Eyes', 'Fly', 'Something of My Own (Project Regeneration)', 'Stay Alive', 'Regeneration', 'Zombie (Live from the NIVA Save Our Stages Festival)', 'Perfect', 'Love Me Again']]


# list1 = []
# list2 = ['Perfect', 'Stay Alive', 'Beautiful Things', 'Love Me Again', 'Sonido Machacas - Acatepec Guerrero Mexico y United State-New York (Pal ft Sain R. Isis Burm K. JJ) England Fix (Live - Streaming)', 'Love and Sex', 'Something of My Own (Project Regeneration)']

list1 = [['ana', 'karen', 'kenia', 'fer'], ['liz', 'jess', 'diana', 'vane'], ['ana', 'karen', 'kenia', 'fer']]
list2 = ['karen', 'fer', 'liz', 'ana']

available = [sublist.copy() for sublist in list1]

indices = []

if len(list1) == 0:
  current_list = example
else:
  current_list = list1

for item in list2:
  for sublist in current_list:
    if item in sublist:
      indices.append(sublist.index(item) + 1)
      break

join_list = [item for sublist in list1 for item in sublist]
indices = [join_list.index(item) + 1 for item in list2]
print(f"\n{join_list}\n{indices}")

random_number = random.randint(1, 4)
# print(random_number)
song_genre = ['Pop', 'Ambient', 'Alternative', 'Dance']
list_song_genres = random.sample(song_genre, random_number)
print(list_song_genres)
gender_list = ', '.join(list_song_genres)
print(gender_list)

print("\n")


import time

def print_radio_art(art_lines, indent=46, char_delay=0.25):
    spacing = " " * indent
    for line in art_lines:
        print(spacing, end="", flush=True)
        for char in line:
            print(char, end="", flush=True)
            time.sleep(char_delay)
        print()  # salto de línea al final de cada línea

# Definimos el arte como lista de líneas
radio_art = [
    "╔═══╗",
    "║███║",
    "║(O)║ ♫ ♪ ♫ ♪",
    "╚═══╝"
]

# Llamamos la función
print_radio_art(radio_art)