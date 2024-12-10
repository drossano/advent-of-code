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
      if tag:  good_updates.append(update_list)
  return good_updates

def main():
  orders = get_orders('example-order.txt')
  updates = get_updates('example-updates.txt')
  good_updates = get_correct_updates(orders,updates)
  print(good_updates)
main()  