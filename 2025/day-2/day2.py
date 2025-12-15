def get_ranges_from_file(file_name):
  with open(file_name, 'r') as data:
    for line in data:
      split_ranges = line.split(',')
      return(split_ranges)




def check_for_repeat(num):
    start_pos = 0
    max_start_pos = len(str(num))//2
    while start_pos <= max_start_pos:
        subset_len = 1
        max_subset_len = len(str(num))//2
        while subset_len <= max_subset_len:
            offset = 1
            max_offset = len(str(num)) -start_pos - subset_len
            while offset <= max_offset:
                is_repeat = all(str(num)[i] == str(num)[i+offset] for i in range (start_pos, start_pos+subset_len))
                return is_repeat
                offset += 1
            subset_len += 1
        start_pos +=1    

print(check_for_repeat(1188511885))




# Your question is really "do all items from x:x+k match items from y:y+k". That is, does a k-length subset occur twice in the line?

# And you want x:x+k non-overlapping with y:y+k. The easy way to do this is to define y as x plus some offset, d. If you assure that k <= d < len(line)-x-k, then you're always looking within the boundaries of the line.

# You'll then vary k from 1 to len(line)//2, looking for various length duplicates at a given offset from each other.

# The offset from x to y, d, will vary between 1 and len(line)-x-k.

# The starting position for x, similarly will vary from 0 to len(line)//2.

# So, the "all" part is something like this: all( line[i] == line[i+d] for i in range(x,x+k) ) for various legal values of d, x and k.
