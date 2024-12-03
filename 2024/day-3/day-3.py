import regex as re

# Part 1 goal is to get total of muls
# a mul is OMLY mul(INT,INT)
# scan through text and retrieve ints in the right sequence as tuples? if dont shows up ignore until do

#   scan throuh text


def get_memory(filename):
  with open(filename) as f:
    memory = f.read()
    return memory
#   find a muls(INT,INT) sequence, don'ts and dos
def find_instructions(corrupted_memory):
  instructions = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", corrupted_memory)
  return instructions

def get_factors_from_instructions(instructions):
  state = True
  factors =  []
  for instruction in instructions:
    if instruction == "don't()":
      state = False
    elif instruction == "do()":
      state = True
    else:
      if state == True:
        factors.append(find_factors(instruction))
  return factors

    

def find_factors(mul_text):
  mul = re.findall(r"[m][u][l][(](\d+)[,](\d+)[)]", mul_text)
  return mul[0]


  
# Multilply each two tuple
def multiply_factors(factors):
  return int(factors[0]) * int(factors[1])


# Add results

def main ():
  total = 0
  memory = get_memory('input.txt')
  instructions = find_instructions(memory)
  factor_list = get_factors_from_instructions(instructions)
  for factors in factor_list:
    product = multiply_factors(factors)
    total += product
  print("Total = ", total)

main()