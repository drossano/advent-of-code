def get_ranges_from_file(file_name):
  with open(file_name, 'r') as data:
    for line in data:
      split_ranges = line.split(',')
      return(split_ranges)




def check_for_repeat(num):
  num_str = str(num)
  if len(num_str) % 2 == 0:
    split_len = int(len(num_str) / 2)
    first_half = num_str[:split_len]
    second_half = num_str[split_len:]
    return first_half==second_half

def str_to_range(range_str):
  range_list = range_str.split('-')
  return range(int(range_list[0]), int(range_list[1]) + 1)



def add_repeats(input):
  repeat_total = 0
  ranges = get_ranges_from_file(input)
  for range_str in ranges:
    this_range = str_to_range(range_str)
    for num in this_range:
      if check_for_repeat(num):
        repeat_total += num
  return repeat_total

print(add_repeats('./input.txt'))