def get_ranges_from_file(file_name):
  with open(file_name, 'r') as data:
    for line in data:
      split_ranges = line.split(',')
      return(split_ranges)

def get_segment_lengths(num_length):
    segment_lengths = []
    for i in range(1, num_length):
        if num_length % i == 0:
          segment_lengths.append(i)
    return segment_lengths


def get_num_str(num):
  return str(num)

def get_segments(segment_length, num_str):
  segments = []
  for i in range(0, len(num_str), segment_length):
    segment_start = i
    segment_end = i + segment_length
    segments.append(num_str[segment_start:segment_end])
  return segments

def check_for_repeat(num):
  num_str = get_num_str(num)
  num_len = len(num_str)
  segment_lengths = get_segment_lengths(num_len)
  for segment_length in segment_lengths:
    segments = get_segments(segment_length, num_str)
    if all(segment == segments[0] for segment in segments):
      return True
      

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

print(add_repeats('2025/day-2/input.txt'))