import numpy as np

def get_word_search(filename):
  with open(filename) as f:
    word_search = f.read().split()
    word_search = [list(line) for line in word_search]
    return np.array(word_search)
def get_verticals(word_search):
  verticals = word_search.T
  return verticals

def get_diags(word_search, direction):
  diags = []
  lengths = {'x': len(word_search[0]), 'y': len(word_search)}
  max_length = lengths[max(lengths)]

    # start from line 0
  k = 0
  for k in range(2 * (max_length)):
  # while k <= 2 * (max_length - 1):
    line = []
    y = lengths['y'] - 1
    if direction == 'ur': 
        y = lengths['y'] - 1
        while y >=0:
          x = k - y
          if x >= 0 and x < lengths['x']:
            line.append(word_search[y][x])
          y -= 1
    if direction == 'dl':
        y = lengths['y'] -1
        while y >= 0:
          x =  k - (lengths['y'] - y)
          if x >= 0 and x < lengths['x']:
            line.append(word_search[y][x])
          y -=1
    if len(line) >= 4:
      diags.append(line)
  return diags

def find_xmas(lines):
  xmases = 0
  for line in lines:
    for index in range(len(line)):
      word = "".join(line[index : index + 4])
      if word == 'XMAS' or word == 'SAMX':
        xmases += 1
  return xmases
 
def find_x_mases(word_search):
  xmases = 0
  for line  in range(1, len(word_search) - 1):
    for letter in range(1, len(word_search[line]) - 1):
      ul = word_search[line - 1][letter - 1]
      dr = word_search[line + 1][letter + 1]
      ur = word_search[line - 1][letter + 1]
      dl = word_search[line + 1][letter - 1]
      if word_search[line][letter] == 'A':
        if ((ul == 'M' and dr == 'S') or (ul == 'S' and dr == 'M')) and ((ur == 'M' and dl == 'S') or (ur == 'S' and dl == 'M')):
          xmases += 1
  return xmases

def main ():
  word_search = get_word_search('input.txt')
  verticals = get_verticals(word_search)
  ur_diags = get_diags(word_search, 'ur')
  dl_diags = get_diags(word_search, 'dl')
  xmases = find_xmas(word_search) + find_xmas(verticals) + find_xmas(ur_diags) + find_xmas(dl_diags)
  print('Part 1:', xmases)
  x_mases = find_x_mases(word_search)
  print('Part 2', x_mases)
  

main()