import time
import sys


unique_songs_list = [['Dua Lipa - Whatcha Doing', 'Dua Lipa - French Exit', 'Dua Lipa - Falling Forever', 'Dua Lipa - Anything For Love', 'Dua Lipa - Maria', 'Dua Lipa - Happy For You', 'Dua Lipa - Illusion - London Sessions']]

current_list = [['Dua Lipa - Illusion', 'Dua Lipa - Illusion - London Sessions', 'Dua Lipa - Illusion - Extended', 'Dua Lipa - Illusion - Instrumental', 'Dua Lipa - Illusion - Acapella', 'Dua Lipa - Physical (feat. Troye Sivan)', 'Dua Lipa - Whatcha Doing', 'Dua Lipa - French Exit', 'Dua Lipa - Falling Forever', 'Dua Lipa - Anything For Love', 'Dua Lipa - Maria', 'Dua Lipa - Happy For You'], ['Green Day - Boulevard of Broken Dreams', 'Green Day - Holiday', 'Green Day - Holiday/Blvd. of Broken Dreams - Demo', 'Green Day - Wake Me Up When September Ends - Demo', 'Green Day - Jesus of Suburbia - Demo', 'Green Day - Jesus of Suburbia', 'Green Day - Favorite Son', 'Green Day - St. Jimmy - Live from VH1 Storytellers', 'Green Day - Boulevard of Broken Dreams - Live at Irving Plaza, New York, NY, 9/21/04', 'Green Day - Are We the Waiting', 'Green Day - St. Jimmy', 'Green Day - Homecoming', 'Green Day - Whatsername', 'Green Day - Too Much Too Soon', 'Green Day - Shoplifter', 'Green Day - Governator', 'Green Day - American Idiot - Live at Makuhari Messe, Tokyo, Japan, 3/19/05', 'Green Day - Jesus of Suburbia - Live at Makuhari Messe, Tokyo, Japan, 3/19/05', 'Green Day - Holiday - Live at Makuhari Messe, Tokyo, Japan, 3/19/05', 'Green Day - Are We the Waiting - Live at Makuhari Messe, Tokyo, Japan, 3/19/05', 'Green Day - St. Jimmy - Live at Makuhari Messe, Tokyo, Japan, 3/19/05', 'Green Day - Boulevard of Broken Dreams - Live at Makuhari Messe, Tokyo, Japan, 3/19/05', 'Green Day - Are We the Waiting - Live from VH1 Storytellers', 'Green Day - Give Me Novacaine - Live from VH1 Storytellers', 'Green Day - Homecoming - Live from VH1 Storytellers', 'Green Day - American Idiot - Demo', 'Green Day - Burnout - 4-track demo', 'Green Day - Chump - 4-track demo', 'Green Day - Pulling Teeth - 4-track demo', 'Green Day - Basket Case - 4-track demo', 'Green Day - She - 4-track demo', 'Green Day - Sassafras Roots - 4-track demo', 'Green Day - When I Come Around - 4-track demo', 'Green Day - In the End - 4-track demo', 'Green Day - F.O.D. - 4-track demo', "Green Day - When It's Time - 4-track demo"], ['Dua Lipa - Whatcha Doing', 'Dua Lipa - French Exit', 'Dua Lipa - Falling Forever', 'Dua Lipa - Anything For Love', 'Dua Lipa - Maria', 'Dua Lipa - Happy For You', 'Dua Lipa - Illusion - London Sessions']]

favorites_list = ['Dua Lipa - Happy For You', 'Dua Lipa - Falling Forever', 'Dua Lipa - Illusion', 'Green Day - Boulevard of Broken Dreams', "Green Day - When It's Time - 4-track demo", 'Dua Lipa - Whatcha Doing']

print(f"\nunique_songs_list\n {unique_songs_list}\n\nlen {len(unique_songs_list)}")

unique_content_data = []
seen2 = set()

for sublist in current_list:
  item = tuple(sublist)
  if item not in seen2:
    seen2.add(item)
    unique_content_data.append(sublist)

final_result = []
seen_sublist = set()

for sublist in unique_content_data:
  not_in_songs_list = [item for item in sublist if item not in unique_songs_list]
  in_songs_list = [item for item in sublist if item in unique_songs_list]
  
  if tuple(not_in_songs_list) and tuple(not_in_songs_list) not in seen_sublist:
    final_result.append(not_in_songs_list)
    seen_sublist.add(tuple(not_in_songs_list))
  if tuple(in_songs_list) and tuple(in_songs_list) not in seen_sublist:
    final_result.append(in_songs_list)
    seen_sublist.add(tuple(in_songs_list))

current_list = final_result
print(f"\ncurrent_list\n {current_list}\n\nlen {len(current_list)}")
print(f"\nfavorites_list\n {favorites_list}\n")

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

print(f"\nindices {indices}\n\n")

# output [12, 9, 1, 1, 36, 7]

"""
        [6, 3, 1, 1, 36, 1]

"""
def print_dots_after(width=46, dot_delay=0.525, duration=7):
  dots_num = int(duration / dot_delay)
  print(" ", end="", flush=True)
  for _ in range(dots_num):
    print(".", end="", flush=True)
    time.sleep(dot_delay)
  print(" ok", flush=True)

def play_spinner():
  initial_spacing = " " * 2
  spinner = ['-', '\\', '|', '/', '-']

  for frame in spinner:
    print(initial_spacing, end="", flush=True)
    sys.stdout.write('\r' + frame)
    sys.stdout.flush()
    time.sleep(1.125)

  print("\n")

play_spinner()
