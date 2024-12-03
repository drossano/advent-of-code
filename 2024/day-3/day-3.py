import regex as re

# Part 1 goal is to get total of muls
# a mul is OMLY mul(INT,INT)
# scan through text and retrieve ints in the right sequence as tuples?
#   scan throuh text

def get_memory(filename):
  with open(filename) as f:
    memory = f.read()
    return memory
#   find a mul(INT,INT) sequence
def find_factors(corrupted_memory):
  muls = re.findall(r"[m][u][l][(](\d+)[,](\d+)[)]", corrupted_memory)
  return muls
  #"[m][u][l][(]\d+[,]\d+[)]"gm
#   add ints to a two tuple



  
# Multilply each two tuple
def multiply_factors(factors):
  return int(factors[0]) * int(factors[1])


# Add results

def main ():
  total = 0
  memory = get_memory('input.txt')
  factor_list = find_factors(memory)
  for factors in factor_list:
    product = multiply_factors(factors)
    total += product
  print("Total = ", total)

main()