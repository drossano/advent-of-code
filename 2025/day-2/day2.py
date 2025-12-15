def get_ranges_from_file(file_name):
  with open(file_name, 'r') as data:
    for line in data:
      split_ranges = line.split(',')
      return(split_ranges)
print(get_ranges_from_file('input.txt')[0])