import math

def get_orders(filename):
  page_orders = []
  with open(filename, 'r') as orders:
    for line in orders:
      page_orders.append([int(num) for num in line.split('|')])
  return page_orders

def get_updates(filename):
  page_updates = []
  with open(filename, 'r') as updates:
    for line in updates:
      page_updates.append([int(num) for num in line.split(',')])
  return page_updates

def get_correct_updates(orders, updates):
  good_updates = []
  for update_list in updates:
      for update in update_list:
        for order in orders:
          update_index = update_list.index(update)
          # if update is order[1] and order[0] is later in the list buh bye!
          if update == order[1] and any(update == order[0] for update in update_list[update_index:]):
            tag = False
            break
          else:
            tag = True
        if tag == False: break
      if tag:  good_updates.append(update_list)
  return good_updates

def get_bad_updates(all_updates, good_updates):
  bad_updates = [update for update in all_updates if update not in good_updates]
  return bad_updates

def fix_bad_updates(scores, updates):
  for update_list in updates:
    while True:
      index = 0
      swaps = 0
      while index < len(update_list):
        if update_list[index]: # > is before update_list[index] in scores
def get_middle_numbers(updates):
  nums = []
  for update in updates:
    mid_index = math.floor(len(update) / 2)
    nums.append(update[mid_index])
  return nums

def get_order(orders):
  scores = dict()
  for order in orders:
    if order[0] in scores:
      scores[order[0]] += 1
    elif order[1] in scores:
      scores[order[1]] -= 1
    elif order[0] not in scores:
      scores[order[0]] = 1
    elif order[1] not in scores:
      scores[order[1]] = - 1
  score_max = max(scores.values())
  for score in scores:
    scores[score] = score_max - scores[score]
  orders = (sorted(scores, key= scores.get))
  return orders

def main():
  orders = get_orders('input-order.txt')
  updates = get_updates('input-updates.txt')
  scores = get_order(orders)
  good_updates = get_correct_updates(orders,updates)
  middle_numbers = get_middle_numbers(good_updates)
  sum_mids = sum(middle_numbers)
  print("Part 1: ", sum_mids)
  bad_updates = get_bad_updates(updates, good_updates)
  fixed_updates = fix_bad_updates(scores,bad_updates)
  fixed_middle_numbers = get_middle_numbers(fixed_updates)
  sum_fixed_mids = sum(fixed_middle_numbers)
  print("Part 2: ", sum_fixed_mids)
main()  