import math

from functools import cmp_to_key

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

def fix_bad_updates(updates):
  fixed_updates = []
  key_func = cmp_to_key(get_order)
  for update_list in updates:
    sorted_update = sorted(update_list, key =key_func)
    fixed_updates.append(sorted_update)
  return fixed_updates

def get_middle_numbers(updates):
  nums = []
  for update in updates:
    mid_index = math.floor(len(update) / 2)
    nums.append(update[mid_index])
  return nums

orders = get_orders('example-order.txt')


def get_order(page1, page2):
    if [page1, page2] in orders:
      return -1
    elif [page2, page1] in orders:
      return 1
    else:
      return 0

def main():
  updates = get_updates('example-updates.txt')
  good_updates = get_correct_updates(orders,updates)
  middle_numbers = get_middle_numbers(good_updates)
  sum_mids = sum(middle_numbers)
  print("Part 1: ", sum_mids)
  bad_updates = get_bad_updates(updates, good_updates)
  fixed_updates = fix_bad_updates(bad_updates)
  fixed_middle_numbers = get_middle_numbers(fixed_updates)
  sum_fixed_mids = sum(fixed_middle_numbers)
  print("Part 2: ", sum_fixed_mids)
main()  