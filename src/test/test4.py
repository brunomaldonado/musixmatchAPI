import sys
from pathlib import Path
import textwrap

from pyfiglet import Figlet

fig = Figlet(font='cosmic')
print(fig.renderText('Be The One'))

# Añadir 'src' al path
src_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(src_dir))

from utils.config import indentation_body


name1 = ['a', 'b', 'c', 'd', 'e', 'f']
name2 = ['g', 'h', 'i', 'b', 'e', 'a']


name1.extend(name2)
# print(f"name1 {name1} {len(name1)}")
# output ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'b', 'e', 'a']

seen = set()
unique_values = []

for name in name1:
  if name not in seen:
    seen.add(name)
    unique_values.append(name)

# print(f"unique_values {unique_values} {len(unique_values)}")
# print("\n\n")
lyrics_songs = {'lyrics_body': "I see the moon, I see 7the moon, I see the moon\nOh, when you're looking at the sun\nYou're not a fool, not a fool, not a fool\nNo, you're not fooling anyone\n\nOh, but when you're gone, when you're gone, when you're gone\nOh baby, all the lights go out\nThinking now that maybe I was wrong, I was wrong, I was wrong\nCome back to me, baby, we can work this out\n\nOh baby, come on, let me get to know you\nJust another chance so that I can show\nThat I won't let you down and run\nNo, I won't let you down and run\n'Cause I could be the one\n\nI could be the one\nI could be the one\nI could be the one\n...\n\n******* This Lyrics is NOT for Commercial use *******\n(1409623852324)"}

# print("\n" + lyrics_songs['lyrics_body'])
spacing_line = " " * 2
max_width = 52
title = "American Idiot - Live at Makuhari Messe, Tokyo, Japan, 3/19/05"
# ˜ ¨ ¯ 
underline1 = "˜" * len(title)

print(f"{spacing_line}{title}")
print(f"{spacing_line}{underline1}")
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