from unit_tester import test
import time

#Write a function to mirror a solution in the Y axis,
def mirrorY(solution):
    L = len(solution)
    NewSolution = []
    for i in range(L):
        NewSolution.append(solution[-(i+1)])
    return NewSolution
#funcion que mirrors a solucion en el X axis
def mirrorX(solution):
    L = len(solution)
    NewSolution = []
    for i, v in enumerate(solution):
        NewSolution.append(L-v-1)
    return NewSolution

#funcion que rotates image by -90, -180, y -270 degrees
def ccw90(solution):
    NewSolution = solution[:]
    L = len(solution) -1
    for i, v in enumerate(solution):
        column = L - v
        NewSolution[column] = i
    return NewSolution

def ccw180(solution):
    solution = ccw90(solution)
    solution = ccw90(solution)
    return solution

def ccw270(solution):
    for i in range(3):
        solution = ccw90(solution)
    return solution

#funcion que gives all in the family
def sym(solution):
    lista = [solution]
    lista.append(ccw270(solution))
    lista.append(ccw180(solution))
    lista.append(ccw90(solution))
    lista.append(mirrorY(solution))
    lista.append(mirrorY(ccw90(solution)))
    lista.append(mirrorX(solution))
    lista.append(mirrorX(ccw90(solution)))
    return lista

def in_family(ls, sol):
    """Returns True if any member of the family of sol is in the list """
    familia = sym(sol)
    for k in range(1, len(familia)):
        if familia[k] in ls:
            return True
    return False

#unique families only
def unique():
    """Returns a list with only unique solutions for 8x8 queens problem"""
    
    lista = main(8)
    nuevaLista = []
    while len(nuevaLista) < 12:

        for i in range(len(lista)):
            if lista[i] not in nuevaLista and not in_family(nuevaLista, lista[i]):
                nuevaLista.append(lista[i])
                   
    return nuevaLista


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main(i):
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(i))     # Generate the initial permutation
    num_found = 0
    tries = 0
    combos = []
    while num_found < 750:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           #print("Found solution {0} in {1} tries.".format(bd, tries))
           if bd not in combos:
               newBD = bd[:]
               combos.append(newBD)
           tries = 0
           num_found += 1
    return combos



print(unique())



