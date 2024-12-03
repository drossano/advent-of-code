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
def find_muls(memory):
  #"[m][u][l][(]\d+[,]\d+[)]"gm
#   add ints to a two tuple

# Multilply each two tuple
# Add results

def main ():
  print(type(get_memory('example.txt')))
        

main()