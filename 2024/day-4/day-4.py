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
  for k in range(2 * (max_length - 1)):
  # while k <= 2 * (max_length - 1):
    line = []
    y = lengths['y'] - 1
    while  y >= 0:
      if direction == 'ur':
        x = k - lengths['y'] - y
      elif direction == 'dl': 
        x = k - y
      if x >= 0 and x < lengths['x']:
        line.append(word_search[y][x])
      y -= 1
    if len(line) > 0:
      diags.append(line)
  return diags
 
def main ():
  word_search = get_word_search('example.txt')
  verticals = get_verticals(word_search)
  ur_diags = get_diags(word_search, 'dl')
  print(ur_diags)


main()