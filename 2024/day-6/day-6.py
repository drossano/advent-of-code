def get_map(file_name):
  with open(file_name, 'r') as map_data:
    map_array = []
    for line in map_data:
      p = list(line)
      map_array.append(p[:-1])
    return map_array

def get_guard_coords_direction(map_array):
  for line in map_array:
    if 'v' in line:
       return {'coords' :[map_array.index(line), line.index('v')], 'dir' : 'down'}
    elif '^' in line:
      return {'coords' :[map_array.index(line), line.index('^')], 'dir' : 'down'}
    elif '<' in line:
      return {'coords' :[map_array.index(line), line.index('<')], 'dir' : 'left'}
    elif '>' in line:
      return {'coords' :[map_array.index(line), line.index('>')], 'dir' : 'right'}

lab_map = get_map('example-input.txt')

guard_coords_dir = get_guard_coords_direction(lab_map)

print(guard_coords_dir)

print(lab_map[guard_coords_dir['coords'][0]][guard_coords_dir['coords'][1]])