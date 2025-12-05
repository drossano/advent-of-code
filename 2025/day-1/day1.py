import re


def file_to_turns(file_name):
  turns = []
  with open(file_name, 'r') as data:
    for line in data:
      split_turn = re.split('(\d+)', line)
      if split_turn[0] == 'L':
        turn = int(split_turn[1])*-1
        turns.append(turn)
      elif split_turn[0]=='R':
        turns.append(int(split_turn[1]))
    return turns
      
def get_password(turns):
  zeroes = 0
  dial_nums = list(range(0,100))
  index = 50
  for turn in turns:
    start_index = index
    #check how many clicks to zero
    if index == 0:
      dist_to_zero = len(dial_nums)
    elif turn > 0:
      dist_to_zero =len(dial_nums) - index
    elif turn < 0:
      dist_to_zero = index
    index += turn
    if (index > len(dial_nums) or index < 0) and start_index != 0:
      zeroes += 1
    index = (index % len(dial_nums))
    print(index)
    if dial_nums[index % len(dial_nums)] == 0:
      zeroes+=1
  return zeroes
    
    
turns =file_to_turns('./input.txt')
print(get_password(turns))