content_data = []
list_favorite_songs = []
list_favorite_artists = []
list_artists_countries = []
example = [['Beautiful Things', 'Sonido Machacas - Acatepec Guerrero Mexico y United State-New York (Pal ft Sain R. Isis Burm K. JJ) England Fix (Live - Streaming)', 'Country Road', 'Love and Sex', 'Zombie', 'When September Ends', 'Memories', 'Love You', 'W. T. F.', 'Beautiful Eyes', 'Fly', 'Something of My Own (Project Regeneration)', 'Stay Alive', 'Regeneration', 'Zombie (Live from the NIVA Save Our Stages Festival)', 'Perfect', 'Love Me Again']]

def indentation_title1(title, width=46, char_delay=0):
  # print(" " * 1, "-" * 53)
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 9

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

def indentation_title3(title, width=46, char_delay=0):
  first_line_prefix = "  "
  current_line = first_line_prefix
  empty_line = " " * (len(first_line_prefix) - 2)
  title_lines = []
  spacing_line = " " * 11
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