import numpy as np

def get_map(file_name):
  map_list = []
  with open(file_name, 'r') as map_data:
    map_list = map_data.read().splitlines()
    for i in range(len(map_list)):
      map_list[i] = list(map_list[i])
    map_array = np.array(map_list)
    return map_array
  
def get_guard_coords_direction(map_array):
  if 'v' in map_array:
    i,j = np.where(map_array == 'v')
    return {'coords' :[i, j], 'dir' : 'down'}
  elif '^' in map_array:
    i = np.where(map_array == '^')
    return {'coords' :i,  'dir' : 'up'}
  elif '<' in map_array:
    i,j = np.where(map_array == '<')
    return {'coords' :[i, j], 'dir' : 'left'}
  elif '>' in map_array:
    i,j = np.where(map_array == '>')
    return {'coords' :[i, j], 'dir' : 'right'}

def walk(map_array, guard_init_pos):
  pos = guard_init_pos
  while get_next_pos(pos)[0] < np.shape(map_array)[0] and get_next_pos(pos)[1] < np.shape(map_array)[1] and get_next_pos(pos)[0] >= 0 and get_next_pos(pos)[1] >= 0:
    coords = pos['coords']
    direction = pos['dir']
    blocked = True
    while blocked:
      next_pos = get_next_pos(pos)
      if map_array[next_pos] == '#':
        direction = turn_clockwise(direction)
        pos['dir'] = direction
      else:
        blocked = False
    map_array[coords] = 'X'
    coords = next_pos
    pos['coords'],pos['dir'] = coords, direction
  map_array[coords] = 'X' 
  locs = np.count_nonzero(map_array== 'X')
  return locs

def turn_clockwise(direction):
  if direction == 'up':
    return 'right'
  if direction == 'down':
    return 'left'
  if direction == 'left':
    return 'up'
  if direction == 'right':
    return 'down'

def get_next_pos(guard_pos):
  direction = guard_pos['dir']
  coords = guard_pos['coords']
  if direction == 'up':
    return (coords[0] - 1, coords[1])
  if direction == 'down':
    return (coords[0] + 1, coords[1])
  if direction == 'left':
    return (coords[0], coords[1] - 1)
  if direction == 'right':
    return (coords[0], coords[1] + 1)

lab_map = get_map('input.txt')
map_0 = lab_map[0]
guard_coords_dir = get_guard_coords_direction(lab_map)

print(walk(lab_map, guard_coords_dir))